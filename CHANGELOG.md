# Change Log

## [Unreleased] - 

## [0.3.3] - 2010-06-01
### Added
- Unicode symbol support

### Updated
- CHANGELOG for previous releases

### Fix
- can set element to empty value
- unit test fails if module fails
- default file param to empty string
- argument parsing for Ansible 2.1
- missing platform data in the Ansible Galaxy meta file

## [0.3.2] - 2016-01-27
### Added
- RPM spec boilerplate

### Fix
- Ansible 2.0.0.2 related errors

## [0.3.1] - 2015-11-23
### Added
- CHANGELOG
- XML pretty print
- XML namespace parameter
- Installation instructions

### Updated
- GitHub repository maintainer from github_rhinception to cmprescott
- module requirements

### Fix
- abort lacks argument
- cannot modify files in home directory
- always returns changed for set element text
- set_children shouldn't always change the xml file
- setting multiple values reports no changes when there is no change in the last value

## [0.3.0] - 2014-07-08
### Added
- set attributes by nesting a dictionary instead of a string

### Updated
- refactor unit tests 

## [0.2.0] - 2014-07-07
### Added
- Python module
- GNU v2 LICENSE
- README with requirements, examples, contact
- unit tests
- Travis continuous integration

[Unreleased]: https://github.com/cmprescott/ansible-xml/compare/0.3.3...HEAD
[0.3.3]: https://github.com/cmprescott/ansible-xml/compare/0.3.2...0.3.3
[0.3.2]: https://github.com/cmprescott/ansible-xml/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/cmprescott/ansible-xml/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/cmprescott/ansible-xml/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/cmprescott/ansible-xml/compare/0154284...0.2.0