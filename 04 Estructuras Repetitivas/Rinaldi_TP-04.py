"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

for i in range(101):
    print(i)

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

numero = int(input("Ingrese un numero: "))
digitos = 0
temp = abs(numero)
while(temp != 0):
    digitos += 1
    temp = temp // 10

print(f"El numero {numero} tiene: {digitos} digitos.")

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

inferior = int(input("Ingrese el limite inferior: "))
superior = int(input("Ingrese el limite superior: "))
suma = 0
for i in range (inferior + 1, superior):
    suma += i

print(f"La suma de los enteros entre {inferior} y {superior} es = {suma}")

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

numero = 1
total = 0
while(numero != 0):
    numero = int(input("Ingrese un numero entero: "))
    total += numero
print(f"Total acumulado = {total}")

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random
aleatorio = random.randint(0,9)
intentos = 0
while(True):
    numero = int(input("Ingrese un numero: "))
    intentos += 1
    if(numero == aleatorio):
        break
    print("Incorrecto. Intente de nuevo.")
print(f"Fueron necesarios {intentos} intentos")

""" 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

for i in range(100, 0, -2):
    print(i)

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

limite = int(input("Ingrese el limite superior: "))
suma = 0
for i in range(0, limite):
    suma += i
print(f"Suma total = {suma}")

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    if(numero < 0):
        negativos += 1
    elif(numero > 0):
        positivos += 1
    
    if(numero % 2 == 0):
        pares += 1
    else:
        impares += 1

print(f"Total positivos: {positivos}")
print(f"Total negativos: {negativos}")
print(f"Total pares: {pares}")
print(f"Total impares: {impares}")

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

cantidad = 10
suma = 0
for i in range(cantidad):
    numero = int(input(f"Ingrese el numero #{i}: "))
    suma += numero

media = suma / cantidad
print(f"La media de los numeros ingresados es: {media}")

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

numero = int(input("Ingrese un numero: "))
negativo = numero < 0
numero = abs(numero)
invertido = 0
while(numero != 0):
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

if(negativo):
    invertido = invertido * -1

print(f"Numero invertido: {invertido}")