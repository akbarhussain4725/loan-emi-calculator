from loan_emi import (
    calculate_emi,
    total_payment,
    total_interest,
    loan_summary,
    validate_inputs
)

principal = 500000
rate = 8
years = 5

validate_inputs(principal, rate, years)

emi = calculate_emi(principal, rate, years)
total = total_payment(emi, years)
interest = total_interest(total, principal)

print(loan_summary(emi, interest, total))