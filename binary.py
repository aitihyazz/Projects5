number = int(input("Enter a number to convert to binary: "))
bn = ""  
n = number 

while n > 0:
    remainder = n % 2
    bn = str(remainder) + bn
    n //= 2


print(f"The binary representation of {number} is: {bn}")

