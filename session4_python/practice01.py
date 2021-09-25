# Funciones recursivas
# Las funciones se invocan a sí mismas

numbers = [1, 2, 3, 4, 5]

# Ciclo For en Python
# for iterador in arreglo:
#    intrucciones

for number in numbers:
     print(number)

# Ciclo for en Java
# for (inicio, límite, incrememto) {
#    instrucciones;
# }

# for (int i = 0; i <= numbers.length; i++) {
#     System.out.println(numbers[i]);
# }
print("---------------------------------\nRecursión")

def imprimirSecuencia(numero):
    numero += 1

    if numero < 6:
        print(numero)
        imprimirSecuencia(numero)
    else:
        print("Llegaste al límite")
        print("Función recursiva terminada")

imprimirSecuencia(0)

