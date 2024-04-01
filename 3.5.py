def compute_commission(sales_amount):
    if sales_amount >= 15000:
        commission = 0.2 * sales_amount
    elif sales_amount >= 1000:
        commission = 0.15 * sales_amount
    else:
        commission = 0.1 * sales_amount
    print("Sales Amount:", sales_amount)
    print("Commission:", commission)

if __name__ == "__main__":
    sales_amount = float(input("Enter Sales Amount: "))
    compute_commission(sales_amount)
