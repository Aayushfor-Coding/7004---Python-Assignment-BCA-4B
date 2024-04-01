def calculate_salary(bs):
    if bs >= 20000:
        da = 0.3 * bs
        hra = 0.2 * bs
    else:
        da = 0.2 * bs
        hra = 0.1 * bs
    total_salary = bs + da + hra
    print("Basic Salary:", bs)
    print("Dearness Allowance (DA):", da)
    print("House Rent Allowance (HRA):", hra)
    print("Total Salary:", total_salary)

if __name__ == "__main__":
    bs = float(input("Enter Basic Salary: "))
    calculate_salary(bs)
