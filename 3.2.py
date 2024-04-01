def check_number(num):
    if num > 0:
        print(num, "is positive")
    elif num < 0:
        print(num, "is negative")
    else:
        print(num, "is zero")

if __name__ == "__main__":
    num = float(input("Enter a number: "))
    check_number(num)
