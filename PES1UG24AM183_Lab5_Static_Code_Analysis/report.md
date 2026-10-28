# Lab 5: Static Code Analysis

## 1. Objective
The objective of this lab is to analyze Python code using Pylint, Bandit, and Flake8, identify coding and security issues, and improve the quality and safety of the program.

## 2. Tools Used
- **Pylint:** Checks code quality, coding conventions, and potential errors.
- **Bandit:** Identifies potential security vulnerabilities in Python code.
- **Flake8:** Checks Python code for style violations and formatting issues.

## 3. Initial Code Analysis
The original `energy_system.py` contained several issues, including missing docstrings, an unused import, a mutable default argument, global state, broad exception handling, file handling without context managers, and the use of `eval()` on user input.

## 4. Changes Made
The following improvements were implemented:
- Added module and function docstrings.
- Removed the unused `sys` import.
- Replaced the mutable default argument with `None`.
- Reduced reliance on global variables by passing meter data explicitly.
- Added validation for negative energy readings and rate increases.
- Replaced `eval()` with safe numeric conversion using `float()`.
- Used context managers and explicit UTF-8 encoding for file operations.
- Added JSON data validation and more specific exception handling.
- Improved formatting and used f-strings.
- Added a main guard to prevent automatic execution when imported.

## 5. Static Analysis Results
The original code was analyzed using Pylint, Bandit, and Flake8. Issues identified by these tools were documented and addressed.

After the changes:
- **Pylint:** 10.00/10.
- **Bandit:** No issues identified.
- **Flake8:** No findings reported.

The before-and-after output files are included separately in the project.

## 6. Conclusion
Static code analysis helped identify code-quality, security, and formatting issues in the original program. Applying the fixes improved readability, error handling, input validation, and file operations. The updated program passed the final checks reported by Pylint, Bandit, and Flake8.