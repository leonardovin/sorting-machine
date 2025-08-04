# Package Sorting System

A Python application that classifies packages into different categories based on their dimensions and weight.

## Overview

This system categorizes packages into three types:
- **STANDARD**: Normal packages that meet size and weight requirements
- **SPECIAL**: Packages that are either bulky OR heavy (but not both)
- **REJECTED**: Packages that are both bulky AND heavy

### Classification Rules

**Bulky Package:**
- Any dimension (width, height, or length) > 150 cm, OR
- Volume > 1,000,000 cubic cm

**Heavy Package:**
- Weight > 20 kg

## Files

- `sort.py` - Main application with sorting logic and interactive interface
- `test_sort.py` - Comprehensive test suite
- `README.md` - This documentation

## Installation

No external dependencies required. This project uses only Python standard library.

**Requirements:**
- Python 3.6 or higher

## Usage

### Interactive Mode

Run the main application to interactively classify packages:

```bash
python sort.py
```

The program will prompt you to enter:
- Width (cm)
- Height (cm) 
- Length (cm)
- Weight (kg)

**Example:**
```
Package Sorting System - Enter package dimensions and weight in centimeters and kilograms respectively.
Enter 'quit' or press Ctrl+C to exit at any time.

Enter width (cm): 100
Enter height (cm): 100
Enter length (cm): 100
Enter weight (kg): 15

Package classification: STANDARD
Package details:
  Dimensions: 100.0 x 100.0 x 100.0 cm
  Volume: 1,000,000 cubic cm
  Weight: 15.0 kg
```

### Programmatic Usage

You can also import and use the functions directly:

```python
from sort import sort, is_bulky, is_heavy

# Classify a package
result = sort(width=200, height=100, length=50, weight=25)
print(result)  # Output: "REJECTED"

# Check individual conditions
bulky = is_bulky(200, 100, 50)  # True
heavy = is_heavy(25)            # True
```

## Input Validation

The system includes comprehensive input validation:

- **Positive values only**: Dimensions and weight must be positive
- **Reasonable limits**: Maximum 10,000 cm for dimensions, 10,000 kg for weight
- **Type validation**: Handles invalid input gracefully with retry prompts
- **Decimal support**: Accepts both integer and decimal values

## Error Handling

The system handles various edge cases:

- Negative values
- Zero dimensions (weight can be zero)
- Extremely large values
- Invalid input types
- User interruption (Ctrl+C)

## Running Tests

### Run All Tests

```bash
python test_sort.py
```

### Run with Verbose Output

```bash
python -m unittest test_sort.py -v
```

### Run Specific Test Class

```bash
python -m unittest test_sort.TestSortMethod -v
```

### Run Specific Test Method

```bash
python -m unittest test_sort.TestSortMethod.test_standard_packages -v
```

## Test Coverage

The test suite includes 14 comprehensive test cases covering:

### Main Sort Function Tests
- ✅ Standard packages (normal size and weight)
- ✅ Bulky packages (large dimensions or volume)
- ✅ Heavy packages (weight > 20 kg)
- ✅ Rejected packages (both bulky and heavy)
- ✅ Edge case boundaries (exact limit values)
- ✅ Error handling (negative, zero, extreme values)
- ✅ Decimal value support

### Individual Function Tests
- ✅ `is_bulky()` function testing
- ✅ `is_heavy()` function testing
- ✅ Error handling for each function

## Example Test Cases

```python
# Standard package
sort(100, 100, 50, 15) → "STANDARD"

# Bulky package (large dimension)
sort(200, 50, 50, 10) → "SPECIAL"

# Heavy package
sort(50, 50, 50, 25) → "SPECIAL"

# Rejected package (bulky AND heavy)
sort(200, 100, 100, 25) → "REJECTED"

# Error handling
sort(-10, 50, 50, 10) → "ERROR: Dimensions must be positive values"
```

## Boundary Conditions

The system uses strict boundaries:
- Dimensions exactly 150 cm = **NOT** bulky
- Dimensions > 150 cm = bulky
- Volume exactly 1,000,000 cubic cm = **NOT** bulky
- Volume > 1,000,000 cubic cm = bulky
- Weight exactly 20 kg = **NOT** heavy
- Weight > 20 kg = heavy

## Contributing

When making changes:
1. Update the relevant functions in `sort.py`
2. Add corresponding test cases in `test_sort.py`
3. Run the test suite to ensure all tests pass
4. Update this README if needed

## License

This project is for educational purposes.
