usuarios = ["Ana", "Luis", "Sofi"]
datos = {"nombre": "Ana", "nivel": 5, "consola": "Xbox"}

print("1. ValueError")
print("2. TypeError")
print("3. ZeroDivisionError")
print("4. IndexError")
print("5. KeyError")
print("6. Salir")

while True:
    try:
        opcion = int(input("\nElige una opcion: "))

        if opcion == 1:
            try:
                edad = int(input("Escribe tu edad: "))
                print("Tu edad es:", edad)
            except ValueError:
                print("Error, tienes que escribir un numero")

        elif opcion == 2:
            try:
                nivel = int(input("Escribe tu nivel: "))
                resultado = nivel + "10"
                print(resultado)
            except TypeError:
                print("Error, no puedes sumar numero con texto")

        elif opcion == 3:
            try:
                puntos = int(input("Escribe tus puntos: "))
                partidas = int(input("Entre cuantas partidas: "))
                promedio = puntos / partidas
                print("Tu promedio es:", promedio)
            except ZeroDivisionError:
                print("Error, no puedes dividir entre 0")
            except ValueError:
                print("Error, tienes que escribir numeros")

        elif opcion == 4:
            try:
                print("Usuarios:", usuarios)
                pos = int(input("Que usuario quieres ver (0, 1 o 2): "))
                print("El usuario es:", usuarios[pos])
            except IndexError:
                print("Error, esa posicion no existe")
            except ValueError:
                print("Error, tienes que escribir un numero")

        elif opcion == 5:
            try:
                print("Datos:", list(datos.keys()))
                clave = input("Que dato quieres ver: ")
                print("El dato es:", datos[clave])
            except KeyError:
                print("Error, esa clave no existe")

        elif opcion == 6:
            print("Saliendo...")
            break

        else:
            print("Esa opcion no existe")

    except ValueError:
        print("Error, tienes que escribir un numero para elegir")