import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area


radio = 5
area_del_circulo = calcular_area_circulo(radio)
print("El área del círculo es:", area_del_circulo)