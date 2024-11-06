# WAP to demonstrate Polymorphism
class Animal: 
    def speak(self): 
        pass 
class Dog(Animal): 
    def speak(self): 
        return "Woof!" 
class Cat(Animal): 
    def speak(self): 
        return "Meow!" 
def make_animal_speak(animal): 
    print(animal.speak()) 
dog = Dog() 
cat = Cat()
make_animal_speak(dog)
make_animal_speak(cat)
print("THIS PROGRAM IS WRITTEN BY Aaryan ERP :- 0221BCA163")