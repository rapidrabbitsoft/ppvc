# PPVC (Python Package Version Checker)

PPVC is a simple and efficient command-line utility that queries PyPI (Python Package Index) for available versions of Python packages. It's designed to be fast, reliable, and easy to use.

## Features

- List all available versions of a Python package
- Get only the latest version of a package
- Simple and intuitive command-line interface
- Fast response times
- Error handling for network issues and non-existent packages
- Beautiful colorized output with formatted tables
- Version type classification (Final, Pre-release, Post-release)

## Installation

You can install PPVC using pip:

```bash
pip install ppvc
```

## Usage

### Basic Usage

List all available versions of a package:

```bash
ppvc requests
```

### Get Latest Version

Show only the latest version of a package:

```bash
ppvc requests --latest
```

### Examples

```bash
# List all versions of the requests package
ppvc requests

# Get the latest version of numpy
ppvc numpy --latest

# Check versions of a specific package
ppvc django
```

## Error Handling

PPVC provides clear error messages for common issues:

- Package not found on PyPI
- Network connection problems
- Invalid package names

## Requirements

- Python 3.7 or higher
- Internet connection to access PyPI
- packaging>=23.0 (for version parsing)
- rich>=13.0.0 (for terminal formatting)

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Run tests (if applicable)
5. Submit a pull request

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the BSD 2-Clause License - see the [LICENSE](LICENSE) file for details.

## Author

Chris McMichael (python@apprabb.it)