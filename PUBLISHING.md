# Publishing PPVC to PyPI

This guide explains how to publish the PPVC package to PyPI (Python Package Index).

## Prerequisites

1. **PyPI Account**: Create an account on [PyPI](https://pypi.org/account/register/)
2. **TestPyPI Account**: Create an account on [TestPyPI](https://test.pypi.org/account/register/) for testing
3. **API Token**: Generate an API token on PyPI for secure uploads

## Manual Publishing

### 1. Install Build Tools

```bash
pip install build twine
```

### 2. Build the Package

```bash
python -m build
```

This creates two distribution files in the `dist/` directory:
- `ppvc-1.0.0.tar.gz` (source distribution)
- `ppvc-1.0.0-py3-none-any.whl` (wheel distribution)

### 3. Test on TestPyPI (Recommended)

First, test your package on TestPyPI:

```bash
twine upload --repository testpypi dist/*
```

Install and test from TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ ppvc
ppvc --help
```

### 4. Publish to PyPI

Once tested, publish to the main PyPI:

```bash
twine upload dist/*
```

## Automated Publishing with GitHub Actions

The repository includes GitHub Actions workflows for automated publishing:

### Setup GitHub Secrets

1. Go to your GitHub repository settings
2. Navigate to "Secrets and variables" → "Actions"
3. Add a new secret named `PYPI_API_TOKEN` with your PyPI API token

### Publishing Process

1. **Create a Release**: 
   - Go to "Releases" in your GitHub repository
   - Click "Create a new release"
   - Tag version (e.g., `v1.0.0`)
   - Add release notes
   - Publish the release

2. **Automatic Deployment**:
   - The GitHub Action will automatically trigger
   - Build the package
   - Upload to PyPI
   - You can monitor progress in the "Actions" tab

## Version Management

### Updating Version

1. Update version in `pyproject.toml`:
   ```toml
   version = "1.0.1"
   ```

2. Update version in `ppvc/ppvc.py`:
   ```python
   version="ppvc 1.0.1"
   ```

3. Create a new release with the updated version tag

### Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH`
- Example: `1.0.0`, `1.0.1`, `1.1.0`, `2.0.0`

## Testing Before Publishing

### Local Testing

```bash
# Build the package
python -m build

# Install locally
pip install dist/*.whl

# Test the command
ppvc --help
ppvc requests --latest
```

### Run Test Script

```bash
python test_ppvc.py
```

## Troubleshooting

### Common Issues

1. **Package Already Exists**: Ensure version number is unique
2. **Authentication Error**: Check your PyPI API token
3. **Build Errors**: Ensure all dependencies are installed
4. **Upload Errors**: Check internet connection and PyPI status

### Useful Commands

```bash
# Check package contents
tar -tzf dist/ppvc-*.tar.gz

# Validate package
twine check dist/*

# Clean build artifacts
rm -rf dist/ build/ *.egg-info/
```

## Security Best Practices

1. **Use API Tokens**: Never use username/password for uploads
2. **TestPyPI First**: Always test on TestPyPI before main PyPI
3. **Review Dependencies**: Ensure all dependencies are secure
4. **Keep Secrets Safe**: Never commit API tokens to version control

## Package Verification

After publishing, verify the package:

```bash
# Install from PyPI
pip install ppvc

# Test functionality
ppvc --version
ppvc requests --latest
```

## Support

If you encounter issues:
1. Check the [PyPI documentation](https://packaging.python.org/tutorials/packaging-projects/)
2. Review GitHub Actions logs
3. Test locally before publishing
4. Use TestPyPI for validation 