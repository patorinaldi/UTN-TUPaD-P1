import math

# Declaración de funciones
""" 1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

def imprimir_hola_mundo():
    print("Hola Mundo!")

""" 2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario"""

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

""" 3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta función con los valores in-
gresados."""

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo. calcular_peri-
metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
bas funciones para mostrar los resultados."""

def calcular_area_circulo(radio):
    return math.pi * radio * radio

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos-
trar el resultado usando esta función."""

def segundos_a_horas(segundos):
    return segundos / 3600

""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun-
ción."""

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta-
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
sultados de forma clara."""

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Indefinida"
    return (suma, resta, multiplicacion, division)

""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
ción para mostrar el resultado con dos decimales."""

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

def celcius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
# 1
imprimir_hola_mundo()
# 2
saludar_usuario(input("Ingrese su nombre: "))
# 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
#4
radio = int(input("Ingrese el radio del circulo: "))
print(f"Area = {calcular_area_circulo(radio)}")
print(f"Perimetro = {calcular_perimetro_circulo(radio)}")
#5 
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas} horas")
#6
tabla_multiplicar(int(input("Ingrese un numero: ")))
#7
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
resultados = operaciones_basicas(num1, num2)
print(f"{num1} + {num2} = {resultados[0]}")
print(f"{num1} - {num2} = {resultados[1]}")
print(f"{num1} * {num2} = {resultados[2]}")
print(f"{num1} / {num2} = {resultados[3]}")
#8
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"IMC = {imc:.2f}")
#9
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = celcius_a_fahrenheit(celsius)
print(f"{celsius}° C = {fahrenheit}° F")
#10
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"Promedio = {promedio}")