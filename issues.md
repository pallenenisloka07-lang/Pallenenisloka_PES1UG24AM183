# Lab 5: Static Code Analysis — Issue Report

| Issue | Type | Line(s) in original code | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe use of `eval()` | Security | 63 | Evaluates user input as Python code and can execute unintended operations. | Replaced `eval()` with numeric input parsing using `float()`. |
| Mutable default argument | Bug | 12 | `history=[]` shares a list across function calls. | Changed the default to `None` and initialized a new list when needed. |
| Bare exception handler | Reliability | 44 | A bare `except` hides unexpected errors. | Handled specific exceptions, including missing files and invalid JSON. |
| Unsafe file handling | Code quality | 42, 48 | Files were opened without context managers or explicit encoding. | Used `with` statements and UTF-8 encoding. |
| Global state modification | Maintainability | 27, 40 | Global variables make functions harder to test and maintain. | Passed meter data and tariff rates as parameters and returned updated values. |
| Missing docstrings | Code quality | Multiple | Functions and the module did not explain their purpose. | Added module and function docstrings. |
| Negative meter readings | Logic | 54–63 | Negative usage could produce unrealistic bills. | Added validation to reject negative readings. |

**Note:** Line numbers refer to the original starter code. The updated file may have different line numbers.
