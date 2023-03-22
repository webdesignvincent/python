ARS = 202.91
COL = 4849.99
MEX = 18.74

def mi_menu():
    print("\n")
    print("***********************************************************")
    print("************CONVERSOR PYTHON CON FUNCIONES*****************")
    print("1.-Dolares estadounidenses a pesos argentinos")
    print("2.-Dolares estadounidenses a pesos colombianos")
    print("3.-Dolares estadounidenses a pesos mexicanos")
    print("***********************************************************")
    print("\n")

def conversor(cons,dolares)->int:
    return cons * dolares

mi_menu()
nombre = input("Ingrese su nombre: ")
opcion = int(input("Seleccione una opcion: "))
dolares = int(input("Cuantos dolares tienes: "))
print("\n")

if opcion == 1:
    print(f"{nombre}, tienes {conversor(ARS,dolares)} pesos argentinos")
elif opcion == 2:
    print(f"{nombre}, tienes {conversor(COL,dolares)} pesos colombianos")
elif opcion == 3:
    print(f"{nombre}, tienes {conversor(MEX,dolares)} pesos mexicanos")
else:
    print(f"{nombre}, No has seleccionado un opcion del menu.Intentar nuevamente.")

    