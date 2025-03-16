# Parent class
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity  # Initialize the seating capacity

    def fare(self):
        return self.capacity * 100  # Calculate the base fare

# Child class
class Bus(Vehicle):
    def __init__(self, capacity=50):
        super().__init__(capacity)  # Initialize the capacity using the parent class

    def fare(self):
        a = super().fare()  # Get the base fare from the parent class
        charge = a * 0.10   # Calculate the maintenance charge (10% of base fare)
        total = charge + a  # Calculate the total fare
        return total       # Return the total fare

# Create a Bus object
bus = Bus()

# Print the total fare
print('Total fare:', bus.fare())