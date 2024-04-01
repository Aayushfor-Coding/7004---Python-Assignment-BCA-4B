# Example using break
num = 1
while num <= 10:
    if num == 5:
        break
    print(num)
    num += 1

# Example using continue
num = 1
while num <= 10:
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1
