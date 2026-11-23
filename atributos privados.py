class bankAccount:
    bank = "teressa calcuta"

    def __init__(self,nombre,contraseña):
        self.nombre_cuenta = nombre
        self.__password = contraseña

    @property
    def contraseña(self):
            return f"{self.__password}"

    @contraseña.setter
    def contraseña(self,nueva_contraseña):
         self.__password = nueva_contraseña

    def __str__(self):
         return f"TITULAR: {self.nombre_cuenta} | Y SU CONTRASEÑA ES: {self.__password}"


cliente = bankAccount("juancho",12345)
print(cliente)

cliente.contraseña = 14523
print("nueva contraseña:")
print(cliente.contraseña)

    