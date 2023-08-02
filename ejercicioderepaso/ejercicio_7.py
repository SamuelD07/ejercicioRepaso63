def encontrar_extremos_lista(lista):
    numero_mas_grande = max(lista)
    numero_mas_pequeno = min(lista)
    return numero_mas_grande, numero_mas_pequeno

lista_numeros = [1, 5, 3, 9, 2]
mayor, menor = encontrar_extremos_lista(lista_numeros)
print("El número más grande es:", mayor)
print("El número más pequeño es:", menor)