def func(a,b):
    return(b-a)
total =int(input("Enter the total bill:"))
given=int(input("Enter the cash given :"))
print("Your change is",func(total,given),"$")