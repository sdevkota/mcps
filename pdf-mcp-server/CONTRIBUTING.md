# Contributing to PDF Tools MCP Server

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🌟 How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Environment details** (OS, Python version)
- **Error messages** or logs

### Suggesting Features

Feature suggestions are welcome! Please provide:

- **Clear use case** for the feature
- **Detailed description** of the functionality
- **Examples** of how it would work
- **Potential implementation** ideas

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 Development Guidelines

### Code Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Keep functions focused and single-purpose
- Add docstrings to all functions

### Type Hints

All functions should include type hints:

```python
def my_function(param1: str, param2: int) -> dict:
    """Function description."""
    return {"result": param1 * param2}
```

### Documentation

Use Google-style docstrings:

```python
def example_function(param1: str, param2: int) -> dict:
    """
    Brief description of the function.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When and why this is raised
    """
    pass
```

### Error Handling

- Use specific exception types
- Provide helpful error messages
- Validate inputs early
- Handle edge cases

### Adding New Tools

To add a new PDF tool:

1. **Add the tool function** to `main.py`:
```python
@mcp.tool
def my_new_tool(param: str) -> dict:
    """
    Description of what the tool does.
    
    Args:
        param: Description
        
    Returns:
        Description of return value
    """
    # Implementation
    return {"result": "success"}
```

2. **Update README.md**:
   - Add tool description to features section
   - Add usage example
   - Update available tools list

3. **Test the tool**:
   - Verify it works as expected
   - Test error cases
   - Check edge cases

## 🧪 Testing

Before submitting a PR:

1. Test your changes manually
2. Ensure no existing functionality is broken
3. Test error cases
4. Verify documentation is updated

## 📋 Commit Messages

Write clear, descriptive commit messages:

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues when relevant

Examples:
```
Add PDF rotation tool

- Implement rotate_pdf function
- Add support for 90, 180, 270 degree rotation
- Update documentation

Fixes #123
```

## 🔍 Code Review Process

All submissions require review:

1. Maintainers will review your PR
2. Address any requested changes
3. Once approved, a maintainer will merge

### Review Criteria

- Code quality and style
- Documentation completeness
- Backward compatibility
- Error handling

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

- Open an issue for discussion
- Check existing documentation
- Reach out to maintainers

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes

Thank you for contributing! 🎉
