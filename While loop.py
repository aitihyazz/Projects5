a = int(input("Enter a number: "))
digit_count = 0

while a > 0:
    a //= 10
    digit_count += 1

print("The number of digits is:", digit_count)

