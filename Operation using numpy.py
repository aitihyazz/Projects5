import numpy as np
myarray =np.array([1,2,3,4,5,6,7,8,9,0] ) 
narray =np.where(myarray%2==1,-1,myarray)
n2array=myarray.reshape(10,1)
result=0
for i in myarray:
    result+= i
    print(result)
print(myarray)
print(narray)
print(n2array)