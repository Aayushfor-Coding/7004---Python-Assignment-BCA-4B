n = int(input("Enter the value of n: "))
a, b = 0, 1
count = 0
print("Fibonacci sequence up to", n, ":")
while count < n:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1
