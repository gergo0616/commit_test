# Git Configuration Setup Guide

This guide explains how to set up a custom Git configuration with a commit message template and default editor settings.

## 1. Git Configuration File Setup

Create or edit your `.gitconfig` file in your home directory with the following structure:

```ini
[commit]
    template = C:/Users/YourUsername/.commit.template

[core]
    editor = notepad
```

## 2. Commit Template Setup

Create a `.commit.template` file in your home directory. This template will be used every time you make a commit:

```
# Title: Summary, imperative, start upper case, don't end with a period
# No more than 50 chars. #### 50 chars is here: #

# Body: Explain *what* and *why* (not *how*). Include task ID (Jira issue).
# Wrap at 72 chars. ################################## which is here: #

# At the end: Include links to any relevant resources, articles, etc.
# --- COMMIT END ---
# Remember to:
#   * Use the imperative mood in the subject line
#   * Limit the subject line to 50 characters
#   * Capitalize the subject line
#   * Do not end the subject line with a period
#   * Separate subject from body with a blank line
#   * Use the body to explain what and why vs. how
#   * Can use multiple lines with "-" for bullet points
```

## 3. Using the Setup

1. When you run `git commit`, Notepad will open automatically with the template
2. Fill in your commit message following the template guidelines
3. Save and close Notepad to complete the commit

## Best Practices for Commit Messages

1. Keep the subject line concise (50 characters or less)
2. Use imperative mood in the subject line
3. Start with a capital letter
4. Don't end the subject line with a period
5. Separate subject from body with a blank line
6. Use the body to explain the what and why of the changes
7. Wrap the body at 72 characters

## File Locations

- `.gitconfig`: Located at `C:/Users/YourUsername/.gitconfig`
- `.commit.template`: Located at `C:/Users/YourUsername/.commit.template`
