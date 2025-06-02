""" Práctico 11: Aplicación de la Recursividad """

""" 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario """

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular factoriales del 1 hasta ese número: "))
print(f"Factoriales del 1 al {numero}:")
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")

print("-" * 50)

""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique. """

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese la posición hasta donde mostrar la serie de Fibonacci: "))
print(f"Serie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")

print("-" * 50)

""" 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula n^m = n * n^(m-1). Prueba esta función en un
algoritmo general. """

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

print("-" * 50)

""" 4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto. """

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero_decimal = int(input("Ingrese un número decimal para convertir a binario: "))
binario = decimal_a_binario(numero_decimal)
print(f"El número {numero_decimal} en binario es: {binario}")

print("-" * 50)

""" 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es. """

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

palabra_test = input("Ingrese una palabra para verificar si es palíndromo: ").lower()
resultado = es_palindromo(palabra_test)
print(f"'{palabra_test}' {'es' if resultado else 'no es'} un palíndromo")

print("-" * 50)

""" 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos. """

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

print("Ejemplos de suma de dígitos:")
print(f"suma_digitos(1234) = {suma_digitos(1234)}")  
print(f"suma_digitos(9) = {suma_digitos(9)}")        
print(f"suma_digitos(305) = {suma_digitos(305)}")    

print("-" * 50)

""" 7) Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide. """

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print("Ejemplos de contar bloques:")
print(f"contar_bloques(1) = {contar_bloques(1)}")  
print(f"contar_bloques(2) = {contar_bloques(2)}")  
print(f"contar_bloques(4) = {contar_bloques(4)}")  

print("-" * 50)

""" 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número. """

def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo_digito = numero % 10
        coincidencia = 1 if ultimo_digito == digito else 0
        return coincidencia + contar_digito(numero // 10, digito)

print("Ejemplos de contar dígito:")
print(f"contar_digito(12233421, 2) = {contar_digito(12233421, 2)}") 
print(f"contar_digito(5555, 5) = {contar_digito(5555, 5)}")          
print(f"contar_digito(123456, 7) = {contar_digito(123456, 7)}")    

print("-" * 50)