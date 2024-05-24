#!/bin/bash

# TODO we need to also add the images and references for the README.md

# Set paths
GITHUB_REPO_URL="https://github.com/Ekumen-OS/andino.git"
CLONE_DIR="./andino_repo"
DEST_DIR="./docs/package_summary"

# Clone the GitHub repository
echo "Cloning repository..."
git clone "$GITHUB_REPO_URL" "$CLONE_DIR"

# Check if the clone was successful
if [ $? -ne 0 ]; then
    echo "Failed to clone repository."
    exit 1
fi

# Find all README.md files and copy them to the destination directory
echo "Copying README.md files..."
mkdir -p "$DEST_DIR"

# Find all README.md files and copy them to the destination directory
echo "Copying README.md files..."
mkdir -p "$DEST_DIR"

find "$CLONE_DIR" -type f -name "README.md" | while read -r readme_path; do
    parent_dir=$(basename "$(dirname "$readme_path")")

    # Skip if the parent directory is 'andino_repo'
    if [ "$parent_dir" == "andino_repo" ]; then
        echo "Skipping $readme_path as it is in the 'andino_repo' directory"
        continue
    fi

    dest_file="$DEST_DIR/${parent_dir}.md"
    cp "$readme_path" "$dest_file"
    if [ $? -eq 0 ]; then
        echo "Copied $readme_path to $dest_file"
    else
        echo "Failed to copy $readme_path"
    fi
done

# Clean up
echo "Cleaning up..."
rm -rf "$CLONE_DIR"

echo "Operation completed successfully!"
