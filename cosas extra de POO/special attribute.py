class animal:
    """class represent an animal"""
    __slots__= ['name', 'age'] # restrict attributes
    species: str = "Unknown" #type annottation
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog = animal("firulais", 5)

print("dog. __class__:", dog.__class__)
print("dog.__module__:", dog.__module__)
print("animal.__doc__:", animal.__doc__)
print("animal.__name__:", animal.__name__)
print("animal.__slots__:",animal.__slots__)
print("animal.__annotations",animal.__annotations__)
print("animal.__bases__:", animal.__bases__)
print("animal.__mro__:", animal.__mro__)
