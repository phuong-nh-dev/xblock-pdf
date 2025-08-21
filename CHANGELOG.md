# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] - 2024-12-19

### Added
- OpenEDX Teak release compatibility
- Python 3.8+ support
- Modern XBlock dependencies (XBlock>=1.6.0, web-fragments>=1.0.0, xblock-utils>=2.0.0)
- Enhanced error handling and logging
- StudioEditableXBlockMixin integration for better studio experience
- Modern development tools (ESLint, Prettier, updated Grunt)
- Comprehensive test suite with pytest
- Tox configuration for multi-version testing
- Better template rendering using XBlock utilities
- Input validation in studio editor
- Improved JavaScript with better error handling

### Changed
- **BREAKING**: Minimum Python version is now 3.8
- **BREAKING**: Updated XBlock dependencies to modern versions
- Replaced Django Template usage with XBlock ResourceLoader
- Modernized JavaScript code with better error handling
- Updated build tools to latest versions
- Improved documentation with development setup instructions

### Fixed
- Template rendering compatibility with newer Django versions
- Event publishing error handling
- JavaScript download tracking functionality
- Studio editor validation and user experience

### Security
- Updated all dependencies to latest secure versions
- Added proper input validation in handlers

## [1.0.0] - Previous Version
- Basic PDF embedding functionality
- Download tracking
- Studio editing interface
