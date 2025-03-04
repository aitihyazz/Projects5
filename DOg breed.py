class dog:
    a='dog','swides'
    def __init__(self,breed,color):
        self.breed=breed
        self.color=color
obj=dog('german','red')
obj1=dog('swides','blue')
print("the featues of german",obj.breed,obj.color)
print('',dog.a,obj.a,obj1.a)
obj1.a='abc'
print('',dog.a,obj.a,obj1.a)
dog.a='abcd'
print('',dog.a,obj.a,obj1.a)

