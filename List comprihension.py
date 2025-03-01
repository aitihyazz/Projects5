n = int(input("Enter the number of elements: "))
my_list = []

for i in range(n):
    element = input("Enter element {}: ".format(i+1))
    my_list.append(int(element)) 

odd = [x for x in my_list if x % 2 == 1] 
print(odd)