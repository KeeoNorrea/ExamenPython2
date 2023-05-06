from Cocteles import Coctele
from Shot import Shots
cocteles = []
shot = []


def funcionCocteles(coctele):

    cantidad = int(input("Cantidad comprada"))
    valorVenta = cantidad * coctel.precio

    if(coctele.frescura == "1"):
        print(f"EL valor de coctel es de: {valorVenta}")
    elif(coctele.frescura == "2"):
        print(f"El valor de coctel es de: {valorVenta *0.8}")
    elif(coctele.frescura == "3"):
        print(f"El valor de coctel es de: {valorVenta *0.5}")
    else:
        print("La cantidad de dias no puede ser mayor a 3")

def funcionShot(shot):

    cantidad = int(input("Cantidad comprada"))
    valorVenta = cantidad * shot.precio
    print(f"El valor de shot es de: {valorVenta}")

while True:
    opcion = int(input("Ingrese 1 para cocteles y 2 para shots: "))

    if(opcion == 1):
        coctel = Coctele()
        coctel.nombre = input("Ingrese el nombre del coctel: ")
        coctel.precio = int(input("Ingrese el precio: "))
        coctel.grados = input("Ingrese el grado de alchol: ")
        coctel.frescura =input("Ingrese la cantidad de dias de frescura: " )
        print(coctel.nombre)
        cocteles.append(coctel)
        funcionCocteles(coctel)
    elif(opcion == 2):
        shot = Shots()

        shot.nombre = input("Ingrese el nombre del coctel: ")
        shot.precio = int(input("Ingrese el precio: "))
        shot.grados = input("gince el grado de alchol: ")
        shot.append(shot)
        funcionShot(shot)
    else:
        print("Esa opcion no existe")
    