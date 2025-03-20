class Ferrari():
    def foundedin(self):
        print("1939")
    def country(self):
        print('Italy')
class BMW():
    def foundedin(self):
        print("1916")
    def country(self):
        print('Germany')
ob1 =Ferrari()
ob2 =BMW()
for i in(ob1,ob2):
    i.foundedin()
    i.country()