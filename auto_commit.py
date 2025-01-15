import subprocess
import os
import time
import sys
from pathlib import Path

def run_git_command(command):
    """Run a git command and return its output"""
    try:
        result = subprocess.run(
            [r'C:\Windows\System32\cmd.exe', '/c', 'git'] + command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)

def get_unstaged_changes():
    """Get the list of unstaged changes"""
    return run_git_command(['status', '--porcelain'])

def create_commit_message(changes):
    """Create a commit message based on the changes"""
    message = "Changes in this commit:\n\n"
    for line in changes.split('\n'):
        if line.strip():
            status = line[:2]
            file = line[3:]
            if status == ' M':
                message += f"- Modified: {file}\n"
            elif status == '??':
                message += f"- Added: {file}\n"
            elif status == ' D':
                message += f"- Deleted: {file}\n"
            elif status == 'M ':
                message += f"- Staged modification: {file}\n"
            elif status == 'D ':
                message += f"- Staged deletion: {file}\n"
            elif status == 'A ':
                message += f"- Staged addition: {file}\n"
    
    return message

def main():
    # Get the repository root
    repo_root = Path(os.getcwd())
    commit_message_path = repo_root / 'commit_message.txt'

    # Get changes
    changes = get_unstaged_changes()
    if not changes:
        print("No changes to commit!")
        return

    # Create commit message
    message = create_commit_message(changes)
    
    # Write to file
    with open(commit_message_path, 'w') as f:
        f.write(message)

    # Open file for editing
    print("Opening commit message for review. Please review and close the file when done.")
    os.startfile(str(commit_message_path))

    # Wait for file to be closed
    last_modified = os.path.getmtime(commit_message_path)
    while True:
        try:
            # Try to open the file in write mode
            with open(commit_message_path, 'r+'):
                current_modified = os.path.getmtime(commit_message_path)
                if current_modified != last_modified:
                    # File has been modified and closed
                    break
        except PermissionError:
            # File is still open
            time.sleep(1)
            continue
        time.sleep(1)

    print("Commit message file closed. Proceeding with commit...")

    # Stage all changes
    run_git_command(['add', '.'])

    # Create commit
    run_git_command(['commit', '-F', str(commit_message_path)])

    # Push changes
    print("Pushing changes to remote repository...")
    run_git_command(['push'])

    print("Changes have been committed and pushed successfully!")

if __name__ == "__main__":
    main()
