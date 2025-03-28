""" 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. """

print("Hola Mundo!")

""" 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”."""

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

""" 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. """

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

""" 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro. """

import math

radio = int(input("Ingrese el radio: "))

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El area del cirulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

""" 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale. """

segundos = int(input("Ingrese cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} hora(s).")

""" 6) Crear un programa que pida al usuario un número e imprima por pantalla
la tabla de multiplicar de dicho número. """

numero = int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(f"{i} x {numero} =",i * numero)

""" 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""

numero1 = int(input("Ingrese un numero distinto a 0: "))
numero2 = int(input("Ingrese otro numero distinto a 0: "))
print(f"{numero1} + {numero2} =",numero1 + numero2)
print(f"{numero1} / {numero2} =",numero1 / numero2)
print(f"{numero1} x {numero2} =",numero1 * numero2)
print(f"{numero1} - {numero2} =",numero1 - numero2)

""" 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. """

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
indice = peso / altura ** 2
print(f"Su indice de masa corporal es = {indice}")

""" 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. """

celsius = int(input("Ingrese temperatura en grados celsius: "))
fahrenheit = 9 / 5 * celsius + 32
print(f"{celsius} grados celsius es = {fahrenheit} grados fahrenheit")

""" 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números. """

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
num3 = int(input("Ingrese tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"Promedio = {promedio}")