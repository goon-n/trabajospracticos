## Ejercicio 1: Dado un número entero, determinar y mostrar la cantidad de dígitos que tiene.

def pedir_numero(tipo="entero"):
    if tipo == "entero":
        return int(input("Ingrese un número entero: "))
    else:
        return float(input("Ingrese un número decimal: "))


def contar_digitos(numero):
    numero = abs(numero)
    return len(str(int(numero)))

def mostrar_cantidad_digitos():
    numero = pedir_numero()
    print(f"El número tiene {contar_digitos(numero)} dígitos.")

## Ejercicio 2: Dado un número decimal, determinar y mostrar la cantidad de dígitos enteros y decimales que tiene.
def contar_digitos_enteros(numero):
    return len(str(abs(int(numero))))

def contar_digitos_decimales(numero):
    parte_decimal = str(numero).split(".")[1] if "." in str(numero) else ""
    return len(parte_decimal)

def mostrar_cantidad_digitos_decimal():
    numero = pedir_numero("decimal")
    enteros = contar_digitos_enteros(numero)
    decimales = contar_digitos_decimales(numero)
    print(f"El número tiene {enteros} dígitos enteros y {decimales} dígitos decimales.")

## Ejercicio 3: Dado N números enteros, cargarlos en un vector, todos distintos de cero, mostrar aquellos elementos que sean compuestos.
def numero_compuesto(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return True
    return False

def pedir_numeros():
    n = int(input("Ingrese la cantidad de números: "))
    numeros = []
    for i in range(n):
        while True:
            numero = int(input(f"Ingrese el número {i + 1} (distinto de 0): "))
            if numero != 0:
                numeros.append(numero)
                break
            print("El número no puede ser 0, intenta de nuevo.")
    return numeros

def mostrar_compuestos():
    numeros = pedir_numeros()
    compuestos = [numero for numero in numeros if numero_compuesto(numero)]
    print(f"Los números compuestos son: {compuestos}")

## Ejercicio 4: Cargar un vector de N elementos enteros, e invertir su contenido utilizando un vector auxiliar.
def invertir_con_auxiliar(vector):
    return vector[::-1]

def pedir_vector():
    n = int(input("Ingrese la cantidad de dígitos en el vector: "))
    return [int(input(f"Ingrese el dígito {i + 1}: ")) for i in range(n)]

def mostrar_inversion():
    vector = pedir_vector()
    print(f"Vector original: {vector}")
    print(f"Invertido (auxiliar): {invertir_con_auxiliar(vector)}")

## Ejercicio 5: Invertir un vector sin utilizar un vector auxiliar.
def invertir_sin_auxiliar(vector):
    inicio, fin = 0, len(vector) - 1
    while inicio < fin:
        vector[inicio], vector[fin] = vector[fin], vector[inicio]
        inicio += 1
        fin -= 1
    return vector

def mostrar_inversion_sin_auxiliar():
    vector = pedir_vector()
    print(f"Vector original: {vector}")
    print(f"Invertido (sin auxiliar): {invertir_sin_auxiliar(vector)}")

## Ejercicio 6: Dada una lista de N números reales, crear y mostrar una lista B con aquellos elementos de A que tengan exactamente 2 dígitos pares y al menos 2 dígitos impares.
def es_par(digito):
    return digito % 2 == 0

def es_impar(digito):
    return not es_par(digito)

def procesar_lista(lista):
    lista_b = []
    for numero in lista:
        digitos = [int(d) for d in str(abs(int(numero)))]
        if sum(1 for d in digitos if es_par(d)) == 2 and sum(1 for d in digitos if es_impar(d)) >= 2:
            lista_b.append(numero)
    return lista_b

def pedir_lista():
    n = int(input("Ingrese la cantidad de números en la lista: "))
    return [float(input(f"Ingrese el número {i + 1}: ")) for i in range(n)]

def mostrar_resultado():
    lista = pedir_lista()
    lista_b = procesar_lista(lista)
    print(f"Lista B con los números que cumplen las condiciones: {lista_b}")

## Ejercicio 7: Insertar un número K luego de cada múltiplo de K en una lista.
def insertar_k(lista, k):
    resultado = []
    for num in lista:
        resultado.append(num)
        if num % k == 0:
            resultado.append(k)
    return resultado

def mostrar_insertar_k():
    lista = pedir_numeros()
    k = int(input("Ingrese el número K: "))
    print(f"Lista modificada: {insertar_k(lista, k)}")

## Ejercicio 8: Dada una matriz de N x M elementos, calcular y mostrar el promedio de cada fila y de cada columna.
def calcular_promedios_matriz():
    m = int(input("Ingrese el número de filas: "))
    n = int(input("Ingrese el número de columnas: "))
    matriz = [[int(input(f"Elemento [{i}][{j}]: ")) for j in range(n)] for i in range(m)]
    print("Matriz ingresada:")
    for fila in matriz:
        print(fila)
    print("Promedios de filas:", [sum(fila) / len(fila) for fila in matriz])
    print("Promedios de columnas:", [sum(matriz[i][j] for i in range(m)) / m for j in range(n)])

## Ejercicio 9: Dado un número de 5 cifras (validar), verificar si la suma de los 2 primeros dígitos es igual a la suma de los 2 últimos.
def verificar_suma_extremos():
    while True:
        numero = input("Ingrese un número de 5 cifras: ")
        if numero.isdigit() and len(numero) == 5:
            suma_inicio = int(numero[0]) + int(numero[1])
            suma_fin = int(numero[3]) + int(numero[4])
            if suma_inicio == suma_fin:
                print("La suma de los dos primeros dígitos es IGUAL a la de los dos últimos.")
            else:
                print("La suma de los dos primeros dígitos es DIFERENTE a la de los dos últimos.")
            break
        else:
            print("Número inválido. Debe tener exactamente 5 cifras.")

## Ejercicio 10: Dado un número N (entero), determinar si es capicúa.
def verificar_capicua():
    numero = input("Ingrese un número entero: ")
    if numero == numero[::-1]:
        print(f"El número {numero} es capicúa.")
    else:
        print(f"El número {numero} no es capicúa.")

## Menú principal
def menu():
    opciones = {
        "1": mostrar_cantidad_digitos,
        "2": mostrar_cantidad_digitos_decimal,
        "3": mostrar_compuestos,
        "4": mostrar_inversion,
        "5": mostrar_inversion_sin_auxiliar,
        "6": mostrar_resultado,
        "7": mostrar_insertar_k,
        "8": calcular_promedios_matriz,
        "9": verificar_suma_extremos,
        "10": verificar_capicua,
    }
    while True:
        print("\nMenú de opciones:")
        for i in range(1, 11):
            print(f"{i}. Ejercicio {i}")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "0":
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción no válida, intente de nuevo.")

menu()
