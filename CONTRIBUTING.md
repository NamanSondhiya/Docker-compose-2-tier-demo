# Contributing to Multi-Tier Docker Application

Thank you for considering contributing to this project! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How Can I Contribute?

### Reporting Bugs

If you find a bug, please create an issue with the following information:

- Clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Environment details (OS, Docker version, etc.)

### Suggesting Enhancements

We welcome enhancement suggestions! Please include:

- Clear and descriptive title
- Detailed description of the proposed enhancement
- Explanation of why this enhancement would be useful
- Possible implementation approach (if you have ideas)

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests if available
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/multi-tier-docker.git
   cd multi-tier-docker
   ```

2. Start the development environment
   ```bash
   docker-compose up -d
   ```

3. Make your changes to the code

4. Test your changes
   ```bash
   # Test backend API
   curl http://localhost:7000/api
   
   # Test frontend
   curl http://localhost:7001
   ```

## Coding Guidelines

### Docker Best Practices

- Use official base images
- Minimize layer count
- Don't run containers as root when possible
- Use multi-stage builds for smaller images

### Python Style Guide

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

## Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests after the first line

## Documentation

- Update the README.md if you change functionality
- Comment your code where necessary
- Update any relevant documentation

## Questions?

Feel free to create an issue with your question or reach out to the maintainers directly.

Thank you for contributing to this project!