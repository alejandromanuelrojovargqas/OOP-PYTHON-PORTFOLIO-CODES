class person:
    def __init__(self,nombre,edad):
        self.name = nombre
        self.age = edad


class mochila:
    def __init__(self,bolsillos,marca,cierres):
        self.bolsillos=bolsillos
        self.marca=marca
        self.cierres=cierres

    def informacion(self):
        print(f"la mochila tiene {self.bolsillos} bolsillos, marca {self.marca}, y {self.cierres} cierres ")



class student(person):
    def __init__(self,nombre,edad,calificacion):
        super().__init__(nombre,edad)
        self.calificacion = calificacion
        self.backpack = mochila


    def show_who_is_he(self):
        print(f"El estudiante es {self.name}, tiene {self.age} años, su calificacion es de {self.calificacion} y tiene una {mochila}")



est1 = student("Manuel", 19, 9.8)
est1.show_who_is_he()
mochi = mochila(4,"totto",5)
mochi.informacion()



