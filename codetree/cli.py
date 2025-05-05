import os
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