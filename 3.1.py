def check_divisibility(num1, num2):
    if num2 == 0:
        print("Error: Cannot divide by zero")
    elif num1 % num2 == 0:
        print(num1, "is divisible by", num2)
    else:
        print(num1, "is not divisible by", num2)

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    check_divisibility(num1, num2)
