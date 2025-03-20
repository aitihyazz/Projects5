tuple1=(1,2,3,4,5,6)
tuple2=(-1,5,3,-9,0)
tuple =[]
for i in range(min(len(tuple1),len(tuple2))):
    tuple.append(tuple1[i]*tuple2[i])
print(tuple)