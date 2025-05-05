import os
import argparse
from collections import defaultdict

def count_lines_of_code(file_path):
    """Counts the number of lines in a file, returns 0 if file cannot be read."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return len(lines)
    except:
        return 0

def print_directory_tree(path):
    """Prints the directory structure with files and their line counts."""
    folder_files = defaultdict(list)

    # Walk through the directory and get files with line counts
    for root, _, files in os.walk(path):
        rel_root = os.path.relpath(root, path)
        folder_name = rel_root if rel_root != '.' else os.path.basename(path)
        for file in sorted(files):
            file_path = os.path.join(root, file)
            lines = count_lines_of_code(file_path)
            if lines > 0:
                folder_files[folder_name].append((file, lines))

    # Print directory tree with line counts
    for folder in sorted(folder_files.keys()):
        print(f"|-- {folder}/")
        for file, lines in folder_files[folder]:
            print(f"    └── {file} -> {lines} lines of code")
        print("")
        
def scan_directory(path):
    """Scans the directory and prints a summary of all files and line counts."""
    total_files = 0
    total_lines = 0

    print(f"\nScanning project folder: {path}\n")
    print_directory_tree(path)

    # Count total files and lines
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            lines = count_lines_of_code(file_path)
            if lines > 0:
                total_files += 1
                total_lines += lines

    print(f"Total files: {total_files}")
    print(f"Total lines of code: {total_lines}")

def main():
    """Main function to handle argument parsing and execution."""
    parser = argparse.ArgumentParser(description="Display folder tree with line counts.")
    parser.add_argument("path", nargs="?", default=".", help="Path to the project directory (default: current)")
    args = parser.parse_args()

    if os.path.exists(args.path):
        scan_directory(args.path)
    else:
        print(f"Path '{args.path}' not found.")