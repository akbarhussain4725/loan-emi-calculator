def validate_inputs(principal, rate, years):
    if principal <= 0:
        raise ValueError("Principal amount must be greater than 0")

    if rate <= 0:
        raise ValueError("Interest rate must be greater than 0")

    if years <= 0:
        raise ValueError("Years must be greater than 0")

    return True