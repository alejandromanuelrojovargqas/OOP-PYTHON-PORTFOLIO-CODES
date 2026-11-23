class person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def greet(self):
        print(f"Hola {person1}, soy {person2}, tengo {self.age} años y vivo en {self.city}")



person1 = person("Juan Francisco",19,"tepic nayarit")
person2 = person ("Amelia Rojas", 21,"saltillo coahuila")
person1.greet(person2)
person2.greet(person1)