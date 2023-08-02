def convertir_fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius

grados_fahrenheit = float(input("Ingresa los grados Fahrenheit: "))
grados_celsius = convertir_fahrenheit_a_celsius(grados_fahrenheit)
print("Los grados Celsius son:", grados_celsius)