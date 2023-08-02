import random

def generar_lista_numeros_aleatorios(cantidad):
    lista = []
    for i in range(cantidad):
        numero = random.randint(1, 100)
        lista.append(numero)
    return lista

cantidad_numeros = 10
lista_numeros_aleatorios = generar_lista_numeros_aleatorios(cantidad_numeros)
print(lista_numeros_aleatorios)