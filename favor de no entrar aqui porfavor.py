class pene:

    negrura = "termino medio"
    pelos = False

    def __init__(self,largo,nombre,):
        self.largo = largo
        self.nombre = nombre
class panochax(pene):
    super().__init__(nombre)  
    def show_info(self):
        print(self.largo,self.negrura,self.pelos,self.nombre)

pene1=pene("5cm","pepinillo rick")
pene1.show_info()
