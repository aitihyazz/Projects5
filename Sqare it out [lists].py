start= int(input('Enter the starting range'))
end=int(input('Enter the ending range'))
squares =[x**2 for x in range(start,end+1) ]
odd= [x for x in squares if x%2 != 0]
even=[x for x in squares if x%2 == 0]
print('Odd numbers',odd)
print('print even numbers',even)