try:
    a=int(input("Enter your age"))
    print("Your age is",a)
except ValueError as ex :
    print("Nuh a",ex)
if a %2 ==0:
        print("Your age is even")    
else:
        print("Your age is odd")  

