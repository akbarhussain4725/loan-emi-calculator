import math

def calculate_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12

    emi = principal * monthly_rate * math.pow(1 + monthly_rate, months)
    emi /= (math.pow(1 + monthly_rate, months) - 1)

    return round(emi, 2)


def total_payment(emi, years):
    return round(emi * years * 12, 2)


def total_interest(total, principal):
    return round(total - principal, 2)