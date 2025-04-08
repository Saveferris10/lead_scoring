#!/bin/bash

# Replace with your GitHub repo URL
REPO_URL="https://github.com/Saveferris10/lead_scoring.git"

# Clone a mirror of the repo (bare clone with full history)
echo "Cloning mirror of repo..."
git clone --mirror $REPO_URL

# Go into the bare repo folder
cd lead_scoring.git

# Run BFG to remove all .env file history
echo "Running BFG Repo-Cleaner to delete .env..."
bfg --delete-files .env

# Clean up reflog and garbage collect
echo "Cleaning reflog and garbage collection..."
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# Force push the cleaned history
echo "Force pushing cleaned repo to GitHub..."
git push --force

echo "✅ Git history cleaned. Return to your working repo and run 'git pull --rebase' to sync."

