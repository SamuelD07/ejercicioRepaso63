def determinar_paridad(numero):
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

numero = int(input("Ingresa un número: "))
resultado = determinar_paridad(numero)
print(resultado)