print("Función recursiva para mostrar una serie numérica en orden descendente")

# Crear función recursiva
def descendente(number):
    
    # number = number -1
    number -= 1

    if number > 0:
        print(number)
        descendente(number)

    else:
        print("Función recursiva terminada")

x = int(input("Ingrese un número positivo mayor a 1: "))
print(x)
descendente(x)