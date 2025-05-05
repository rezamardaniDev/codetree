import os

def count_lines_of_code(file_path):
    """Counts the number of lines in a file, returns 0 if file cannot be read."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return len(lines)
    except:
        return 0
