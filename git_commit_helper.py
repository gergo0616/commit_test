import subprocess
import sys
from datetime import datetime
import re

def run_git_command(command):
    try:
        # Using direct git command without cmd.exe
        result = subprocess.run(['git'] + command,
                              capture_output=True,
                              text=True,
                              check=True,
                              shell=True)  # Added shell=True for Windows
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e.stderr}")
        sys.exit(1)

def get_changed_files():
    """Get list of modified, added, and deleted files"""
    status = run_git_command(['status', '--porcelain'])
    changes = {'modified': [], 'added': [], 'deleted': []}
    
    for line in status.split('\n'):
        if not line:
            continue
        status_code = line[:2]
        file_path = line[3:]
        
        if status_code == ' M' or status_code == 'M ':
            changes['modified'].append(file_path)
        elif status_code == 'A ':
            changes['added'].append(file_path)
        elif status_code == ' D' or status_code == 'D ':
            changes['deleted'].append(file_path)
    
    return changes

def get_diff_summary():
    """Get a summary of changes in modified files"""
    diff = run_git_command(['diff', '--staged'])
    return diff

def generate_commit_message():
    changes = get_changed_files()
    
    if not any(changes.values()):
        print("No changes to commit!")
        sys.exit(0)
    
    # Build commit message
    message_parts = []
    
    # Add summary line
    total_files = sum(len(files) for files in changes.values())
    message_parts.append(f"Update: Changes in {total_files} file(s)")
    
    # Add details for each change type
    for change_type, files in changes.items():
        if files:
            message_parts.append(f"\n{change_type.capitalize()}:")
            for file in files:
                message_parts.append(f"- {file}")
    
    # Add timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message_parts.append(f"\n\nTimestamp: {timestamp}")
    
    return '\n'.join(message_parts)

def main():
    # Stage all changes first
    run_git_command(['add', '.'])
    
    # Generate and show commit message
    commit_message = generate_commit_message()
    print("\nProposed commit message:")
    print("-" * 50)
    print(commit_message)
    print("-" * 50)
    
    # Commit changes
    try:
        run_git_command(['commit', '-m', commit_message])
        print("\nChanges committed successfully!")
    except Exception as e:
        print(f"Error committing changes: {e}")

if __name__ == "__main__":
    main()
