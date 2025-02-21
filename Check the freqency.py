hi ={"I":2,"am":2,"a":3,"student":2}
print("Original dic"+str(hi))
a=0 
K =2
for key in hi:
    if hi[key]==K:
        a=a+1
print("The frequency of hi is",a)