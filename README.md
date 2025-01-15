# Git Commit Helper

This script automates the process of creating meaningful git commit messages based on your repository changes.

## Features

- Automatically detects modified, added, and deleted files
- Generates structured commit messages with:
  - Summary of changes
  - List of modified files
  - List of added files
  - List of deleted files
  - Timestamp of the commit

## Usage

1. Make your changes to the repository
2. Run the script:
   ```
   python git_commit_helper.py
   ```
3. The script will:
   - Stage all changes
   - Generate a commit message
   - Show you the proposed message
   - Commit the changes

## Requirements

- Python 3.6+
- Git installed and configured
- Windows operating system
