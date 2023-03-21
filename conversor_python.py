ARS = 202.91
COL = 4849.99
MEX = 18.74

print("*********************************************")
print("************CONVERSOR PYTHON*****************")
print("1.-Dolares estadounidenses a pesos argentinos")
print("2.-Dolares estadounidenses a pesos colombianos")
print("3.-Dolares estadounidenses a pesos mexicanos")
print("*********************************************")
print("\n")

nombre = input("Ingrese su nombre:")
opcion = int(input("Sellecione una opcion:"))
print("\n")

if opcion == 1:
    dolares = int(input("Cuantos dolares tienes:"))
    pesos =  ARS * dolares
    print(f"tienes {pesos} pesos argentinos")
elif opcion== 2:
    dolares = int(input("Cuantos dolares tienes:"))
    pesos =  COL * dolares
    print(f"tienes {pesos} pesos colombianos")
elif opcion== 3:
    dolares = int(input("Cuantos dolares tienes:"))
    pesos =  MEX * dolares
    print(f"tienes {pesos} pesos mexicanos")
else:
    print(f"{nombre}, No has seleccionado un opcion del menu.Intentar nuevamente.")
