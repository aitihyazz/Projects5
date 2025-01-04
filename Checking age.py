a = int(input("What is your age?: "))
if a <= 20:
    if a < 10:
        print("You are under 10")
    elif a >= 10:  
        print("You are between 10-20")
else:
    print("You are over 20")