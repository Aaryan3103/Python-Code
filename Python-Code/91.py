# WAP to demonstrate Inheritance
class Vehicle: 
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year
    
    def display_info(self): 
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle): 
    def __init__(self, make, model, year, fuel_type): 
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    
    def display_info(self): 
        super().display_info()
        print(f"Fuel type: {self.fuel_type}")

my_car = Car("Toyota", "Corolla", 2020, "Petrol")
my_car.display_info()
print("THIS PROGRAM IS WRITTEN BY Aaryan ERP :- 0221BCA163")