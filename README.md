# Codetree

Codetree is a Python tool that helps you count the lines of code in your project directory. It supports multiple programming languages and provides a detailed breakdown of the number of lines in your project files. Perfect for analyzing and tracking the size of your codebase in an easy-to-read format.

## Features

- Counts lines of code for a wide variety of programming languages.
- Skips hidden files and directories (those starting with a \.dot).
- Provides a summary of total lines of code and file count.
- Supports command-line interface (CLI) for easy integration.

## Installation

### Using pip

Install Codetree directly from PyPI using pip:

```bash
pip install codetree
```

### Manual Installation

To install Codetree manually, clone the repository and use pip:

```bash
git clone https://github.com/rezamardaniDev/codetree.git
cd codetree
pip install .
```

## Usage

Use Codetree via the command-line interface (CLI). Run the following command in your terminal:

```bash
codetree /path/to/your/project
```

This scans the specified directory (or current directory by default) and outputs the number of lines of code in each file, plus a summary of total lines.

### Example

```bash
$ codetree .
Scanning directory: .
|-- src/
|    └── main.py -> 150 lines of code
|    └── utils.py -> 85 lines of code
|
|-- test/
|    └── test_main.py -> 25 lines of code
|
Total files checked: 3
Total lines of code: 260
Total folders: 2
```

## Options

- **Path**: Specify the project directory as an argument. If no path is provided, the current directory (\.) is used by default.

```bash
codetree /path/to/project
```

## Contributing

We welcome contributions to Codetree! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new pull request.

If you find a bug or want to add a feature, feel free to open an issue or submit a pull request!