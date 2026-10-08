class Animal:
    def eat(self):
        print("the animal is eaing")

class Cat(Animal):
    def meow(self):
        print("the cat is meowing")

cat1 = Cat()
cat1.eat()
cat1.meow()
