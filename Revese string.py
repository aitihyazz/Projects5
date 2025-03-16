class strung():
    def __init__(self,s=''):
        self.s =s
    def input(self):
        return self.s[::-1]
inpu=input('enter a string:')
Obj1=strung(inpu)
a=Obj1.input()
print(a)