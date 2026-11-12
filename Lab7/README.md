# L6_L7_03 — Coffee Shop Order

## Lab 7: Fuzz Testing with Hypothesis

### About

This project demonstrates fuzz testing and input validation using the **Hypothesis** Python library.

Property-based tests are used to test the coffee shop order processor with different inputs, including empty strings, invalid values, and unexpected data types.

The testing focuses on:
- Drink menu code lookups
- Espresso shot cost calculations
- Order modifier parsing

The application was updated to handle invalid inputs safely and prevent unhandled exceptions.

### Files

| File | Description |
|---|---|
| `processor.py` | Updated coffee shop order processing application with input validation |
| `test_processor.py` | Hypothesis-based fuzz tests for testing different input values |
| `Lab7_Report_Palleneni_Sloka.pdf` | Lab 7 report with experiment details and results |
| `Lab7_Screenshots.pdf` | Screenshots showing original output, failing tests, fixed output, and passing tests |

### Testing

Install the required libraries:

```bash
pip install hypothesis pytest
```

Run the tests:

```bash
pytest -v test_processor.py
```

### Results

- Initial fuzz testing identified input-handling errors.
- The application was modified to handle invalid inputs safely.
- All three property-based tests passed after the fixes.

### Conclusion

Fuzz testing with Hypothesis helped identify unexpected input-handling issues and improve the reliability of the coffee shop order processing application.

All Lab 7 deliverables are maintained in the `Lab7` folder.
