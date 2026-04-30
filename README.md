
# Loan EMI Calculator

A simple Python package to calculate loan EMI, total interest, and total payment.

## Features
- EMI calculation
- Total interest calculation
- Total payment summary
- Input validation

## Installation

```bash
pip install loan-emi
```

## Usage

```python
from loan_emi import calculate_emi, total_payment, total_interest

emi = calculate_emi(500000, 8, 5)
total = total_payment(emi, 5)
interest = total_interest(total, 500000)

print(emi, total, interest)
```

## Project Structure

loan_emi/
- calculator.py
- summary.py
- validator.py

## License
MIT

# loan-emi-calculator

