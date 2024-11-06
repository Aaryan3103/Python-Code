# WAP to demonstrate Encapsulation
class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
    
    def display_info(self):
        print(f"{self._year} {self._make} {self._model}")
    
    def set_year(self, year):
        if year > 1885:
            self._year = year
        else:
            print("Invalid year")
    
    def __str__(self):
        return f"{self._year} {self._make} {self._model}"

car = Car("Tesla", "Model S", 2023)
car.display_info()
car.set_year(1880)
car.set_year(2025)
print(car)
print("THIS PROGRAM IS WRITTEN BY Aaryan ERP :- 0221BCA163")