# WAP to demonstrate Abstraction
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
print("THIS PROGRAM IS WRITTEN BY Aaryan ERP :- 0221BCA163")