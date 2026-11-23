class empleado:
    empresa = "TechCorp"

    def __init__(self,nombre,sueldo,horas_trabajadas):
        self.nombre = nombre
        self.__sueldo = sueldo
        self.horas_trabajadas= horas_trabajadas


    @classmethod
    def cambiar_empresa(cls,nueva_emp):
        cls.empresa = nueva_emp

    @staticmethod
    def es_sueldo_valido(sueldo):
        return sueldo > 0
    

    def get_sueldo(self):
        return self.__sueldo

    def set_sueldo(self, nuevo_sueldo):
        if nuevo_sueldo > 0:
            self.__sueldo = nuevo_sueldo
        else:
            print("Error: El sueldo debe ser mayor a 0$")

    def calcular_pago(self):
        return self.get_sueldo()

    def __str__(self):
        return f"Empleado: {self.nombre} | empresa: {self.empresa}"

    def __len__(self):
        return self.horas_trabajadas
    


class gerente(empleado):
    def __init__(self,nombre,sueldo,horas_trabajadas,departamento):
        super().__init__(nombre,sueldo,horas_trabajadas)
        self.departamento = departamento

    def calcular_pago(self):
        return self.get_sueldo() + 5000



emp1 = empleado("Ana Marcela", 23000,40)
ger1 = gerente("Geremias Robles",40000,35,"ventas")

print("-----------------------------------------")
print(emp1)
print("horas trabajadas:", len(emp1))
print("el pago de Ana es de:", emp1.calcular_pago(),"pesos")


print("-----------------------------------------")
print(ger1)
print("horas trabajadas:", len(ger1))
print("el pago de Geremy es de:", ger1.calcular_pago(),"pesos")

ger1.set_sueldo(55000)
print("Nuevo sueldo de geremy:", ger1.get_sueldo())
        


