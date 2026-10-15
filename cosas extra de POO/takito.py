
class animal():
    type_animal = "mammal"
    breathes= True

    def __init__ (self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def eat (self):
        print(f"{self.name} is eating")

class Cat(animal):
    def meow(self):
        print(f"{self.name} is meowing")

    print("---------")
    object1 = cat("fechito", "feline", 6)
    object1 = eat()
    object1 = meow()