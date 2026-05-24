

def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertimos a minúsculas
    return palabra == palabra[::-1]  # Comparamos con su reverso

print(es_palindromo("0scar"));
print(es_palindromo("Anana"));

def es_primo(n):
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Tiene un divisor, no es primo
    return True  # No tiene divisores, es primo


def es_mayor_de_edad(edad):
    if edad < 0:
        return "Edad no válida"
    return edad >= 18