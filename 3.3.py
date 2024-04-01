def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    check_leap_year(year)
