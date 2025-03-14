class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity  

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, capacity=50):
        super().__init__(capacity)

    def fare(self):
        a = super().fare()
        charge = a * 0.10
        total = charge + a
        return total

bus = Bus()
print('Total fare:', bus.fare())