# Lab 5: Static Code Analysis — Reflection

### 1. What is the purpose of static code analysis?

Static code analysis examines source code without executing it. It helps identify potential bugs, security vulnerabilities, and style violations before the program runs.

### 2. What did Pylint, Bandit, and Flake8 help identify?

Pylint identified code-quality issues such as missing docstrings, mutable default arguments, global statements, and unsafe use of `eval()`. Bandit checks for common security vulnerabilities, while Flake8 checks formatting and compliance with Python style guidelines.

### 3. How did you fix the issues found?

I replaced `eval()` with numeric input parsing, removed the mutable default argument, improved exception handling, used context managers for file operations, reduced global state, added docstrings, and corrected formatting. I also added validation to reject negative meter readings.

### 4. How did static analysis improve the program?

Static analysis helped improve code readability, maintainability, and security. After making changes, Pylint reported a score of 10.00/10, Bandit reported no issues, and Flake8 reported no errors.

