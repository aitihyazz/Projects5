class Circle:
    def __init__(self,radius):
        self.radius=radius
    def parameter(self):
        a=self.radius*2*3.1216
        print('Peimeter',a)
    def area(self):
        b=self.radius*self.radius*3.1416
        print('area',b)
cir = Circle(2)
cir.parameter()  
cir.area()