import os
import argparse
from collections import defaultdict

def is_text_file(file_path):
    """Check if a file is a text file based on its content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read()
        return True
    except (UnicodeDecodeError, IOError):
        return False

def count_lines_of_code(file_path):
    """Counts the number of lines in a file if it's a text file."""
    if not is_text_file(file_path):
        return 0  # Skip non-text files
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return len(lines)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def print_directory_tree(path):
    """Prints the directory structure with files and their line counts."""
    folder_files = defaultdict(list)
    folder_count = 0
    checked_files = 0

    # Walk through the directory and get files with line counts
    for root, dirs, files in os.walk(path):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        rel_root = os.path.relpath(root, path)
        folder_name = rel_root if rel_root != '.' else 'root'  # Show root separately
        folder_count += 1
        
        for file in sorted(files):
            if file.startswith('.'):
                continue
            
            file_path = os.path.join(root, file)
            lines = count_lines_of_code(file_path)
            if lines > 0:
                folder_files[folder_name].append((file, lines))
                checked_files += 1

    # Print directory tree with line counts
    for folder in sorted(folder_files.keys()):
        print(f"|-- {folder}/")
        for file, lines in folder_files[folder]:
            print(f"    └── {file} -> {lines} line")
        print("")

    return folder_count, checked_files

def scan_directory(path):
    """Scan the directory and prints summary of files and line counts."""
    print(f"\nScanning directory: {path}")
    total_lines = 0

    folder_count, checked_files = print_directory_tree(path)

    # Count total lines
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.startswith('.'):
                continue
            
            file_path = os.path.join(root, file)
            lines = count_lines_of_code(file_path)
            total_lines += lines

    print(f"\nTotal files checked: {checked_files}")
    print(f"Total lines of code: {total_lines}")
    print(f"Total folders: {folder_count}")

def main():
    """Main function to handle argument parsing and execution."""
    parser = argparse.ArgumentParser(description="Count lines of code in a project directory.")
    parser.add_argument('path', nargs='?', default=".", help="Path to the project directory (default: current directory)")
    args = parser.parse_args()

    print(f"Checking path: {args.path}")
    if os.path.exists(args.path):
        scan_directory(args.path)
    else:
        print(f"Path '{args.path}' not found.")

if __name__ == "__main__":
    main()
