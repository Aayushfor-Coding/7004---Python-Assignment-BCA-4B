def calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate/100) ** time)

if __name__ == "__main__":
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (per annum): "))
    time = float(input("Enter time period (in years): "))

    compound_interest = calculate_compound_interest(principal, rate, time)

    print("Compound interest:", compound_interest)
