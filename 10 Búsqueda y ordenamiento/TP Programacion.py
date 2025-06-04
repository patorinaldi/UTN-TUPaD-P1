"""
Algoritmos de Búsqueda y Ordenamiento
Trabajo Integrador - Programación I
"""

import time

personas = [] 

def bubble_sort(lista):
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]: 
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    
    return lista_copia

def selection_sort(lista):
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista_copia[j] < lista_copia[min_idx]: 
                min_idx = j
        if min_idx != i:
            lista_copia[i], lista_copia[min_idx] = lista_copia[min_idx], lista_copia[i]
    
    return lista_copia

def insertion_sort(lista):
    lista_copia = lista.copy()
    
    for i in range(1, len(lista_copia)):
        key = lista_copia[i]
        j = i - 1
        while j >= 0 and lista_copia[j] > key:
            lista_copia[j + 1] = lista_copia[j]
            j -= 1
        lista_copia[j + 1] = key
    
    return lista_copia

def busqueda_lineal(lista, nombre_buscado):
    posiciones = []
    for i, nombre in enumerate(lista):
        if nombre.lower() == nombre_buscado.lower(): 
            posiciones.append(i)
    return posiciones

def busqueda_binaria(lista, nombre_buscado):
    lista_ordenada = sorted(lista)
    low = 0
    high = len(lista_ordenada) - 1
    posiciones = []
    
    while low <= high:
        mid = (low + high) // 2
        if lista_ordenada[mid].lower() == nombre_buscado.lower():
            posiciones.append(mid)
            left = mid - 1
            while left >= 0 and lista_ordenada[left].lower() == nombre_buscado.lower():
                posiciones.append(left)
                left -= 1
            right = mid + 1
            while right < len(lista_ordenada) and lista_ordenada[right].lower() == nombre_buscado.lower():
                posiciones.append(right)
                right += 1
            break
        elif lista_ordenada[mid].lower() < nombre_buscado.lower():
            low = mid + 1
        else:
            high = mid - 1
    
    return posiciones, lista_ordenada

def cargar_datos_manual():
    global personas
    print("\n=== CARGA DE DATOS ===")
    try:
        cantidad = int(input("¿Cuántos nombres desea ingresar? "))
        personas = [] 
        
        for i in range(cantidad):
            print(f"\nPersona {i + 1}:")
            nombre = input("Nombre: ").strip()
            while not nombre:
                nombre = input("Por favor, ingrese un nombre válido: ").strip()
            
            personas.append(nombre)
        
        print(f"\n✓ Se cargaron {len(personas)} nombres correctamente.")
    except ValueError:
        print("Error: Ingrese un número válido.")

def cargar_datos_ejemplo():
    global personas
    personas = [
        "Ana", "Carlos", "Beatriz", "David", "Elena", "Fernando", 
        "Gabriela", "Hugo", "Isabel", "Javier", "Ana", "Carlos",
        "Lucia", "Miguel", "Natalia", "Oscar", "Patricia", "Roberto", 
        "Sofia", "Tomas", "Valeria", "Walter", "Ximena", "Yamil",
        "Zoe", "Adrian", "Bianca", "Cesar", "Diana", "Eduardo", 
        "Fernanda", "Gabriel", "Helena", "Ignacio", "Julia", "Kevin",
        "Laura", "Martin", "Nina", "Omar", "Paola", "Quintin", 
        "Rosa", "Sebastian", "Teresa", "Ulises", "Victoria", "William",
        "Yolanda", "Zacarías"
    ]
    print(f"✓ Se cargaron {len(personas)} nombres de ejemplo.")

def mostrar_lista():
    if not personas:
        print("No hay nombres cargados.")
        return
    
    print("\n=== LISTA DE NOMBRES ===")
    for i, nombre in enumerate(personas):
        print(f"{i + 1}. {nombre}")

def medir_tiempo_ejecucion(func, *args):
    inicio = time.perf_counter()
    resultado = func(*args)
    fin = time.perf_counter()
    tiempo = (fin - inicio) * 1000000  # Convertir a microsegundos
    return resultado, tiempo

def mostrar_lista_ordenada(lista_ordenada, titulo):
    print(f"\n{titulo}:")
    for i, nombre in enumerate(lista_ordenada):
        print(f"{i + 1}. {nombre}")

# ==================== MENÚS PRINCIPALES ====================

def menu_ordenamiento():
    if not personas:
        print("No hay datos cargados. Cargue datos primero.")
        return
    
    print("\n=== ALGORITMOS DE ORDENAMIENTO ===")
    print("1. Bubble Sort (alfabético)")
    print("2. Selection Sort (alfabético)")
    print("3. Insertion Sort (alfabético)")
    print("0. Volver al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opción: "))
        
        if opcion == 0:
            return
        
        if opcion == 1:
            lista_ordenada, tiempo = medir_tiempo_ejecucion(bubble_sort, personas)
            print(f"\n✓ Bubble Sort completado:")
            mostrar_lista_ordenada(lista_ordenada, "Lista ordenada alfabéticamente")
            
        elif opcion == 2:
            lista_ordenada, tiempo = medir_tiempo_ejecucion(selection_sort, personas)
            print(f"\n✓ Selection Sort completado:")
            mostrar_lista_ordenada(lista_ordenada, "Lista ordenada alfabéticamente")
            
        elif opcion == 3:
            lista_ordenada, tiempo = medir_tiempo_ejecucion(insertion_sort, personas)
            print(f"\n✓ Insertion Sort completado:")
            mostrar_lista_ordenada(lista_ordenada, "Lista ordenada alfabéticamente")
            
        else:
            print("Opción no válida.")
            return
        
        print(f"\nTiempo de ejecución: {tiempo:.2f} μs")
        
    except ValueError:
        print("Error: Ingrese un número válido.")

def menu_busqueda():
    if not personas:
        print("No hay datos cargados. Cargue datos primero.")
        return
    
    print("\n=== ALGORITMOS DE BÚSQUEDA ===")
    print("1. Búsqueda lineal por nombre")
    print("2. Búsqueda binaria por nombre")
    print("0. Volver al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opción: "))
        
        if opcion == 0:
            return
        
        if opcion == 1:
            nombre = input("Ingrese el nombre a buscar: ").strip()
            if not nombre:
                print("Nombre no válido.")
                return
            
            posiciones, tiempo = medir_tiempo_ejecucion(busqueda_lineal, personas, nombre)
            print(f"\n✓ Búsqueda lineal por nombre completada:")
            print(f"Tiempo de ejecución: {tiempo:.2f} μs")
            
            if posiciones:
                print(f"Encontrado en {len(posiciones)} posición(es):")
                for pos in posiciones:
                    print(f"Posición {pos + 1}: {personas[pos]}")
            else:
                print(f"No se encontró ninguna persona con el nombre '{nombre}'.")
        
        elif opcion == 2:
            nombre = input("Ingrese el nombre a buscar: ").strip()
            if not nombre:
                print("Nombre no válido.")
                return
            
            resultado, tiempo = medir_tiempo_ejecucion(busqueda_binaria, personas, nombre)
            posiciones, lista_ordenada = resultado
            print(f"\n✓ Búsqueda binaria por nombre completada:")
            print(f"Tiempo de ejecución: {tiempo:.2f} μs")
            print("(Nota: La lista fue ordenada automáticamente para la búsqueda binaria)")
            
            if posiciones:
                print(f"Encontrado en {len(posiciones)} posición(es) en la lista ordenada:")
                for pos in sorted(posiciones):
                    print(f"Posición {pos + 1}: {lista_ordenada[pos]}")
            else:
                print(f"No se encontró ninguna persona con el nombre '{nombre}'.")
        
        else:
            print("Opción no válida.")
            
    except ValueError:
        print("Error: Ingrese un número válido.")

def menu_principal():
    while True:
        print("\n" + "="*50)
        print(" ALGORITMOS DE BÚSQUEDA Y ORDENAMIENTO")
        print("="*50)
        print("1. Cargar datos manualmente")
        print("2. Cargar datos de ejemplo")
        print("3. Mostrar lista actual")
        print("4. Algoritmos de ordenamiento")
        print("5. Algoritmos de búsqueda")
        print("0. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            
            if opcion == 0:
                print("¡Gracias por usar el programa!")
                break
            elif opcion == 1:
                cargar_datos_manual()
            elif opcion == 2:
                cargar_datos_ejemplo()
            elif opcion == 3:
                mostrar_lista()
            elif opcion == 4:
                menu_ordenamiento()
            elif opcion == 5:
                menu_busqueda()
            else:
                print("Opción no válida. Intente nuevamente.")
                
        except ValueError:
            print("Error: Ingrese un número válido.")
        
        input("\nPresione Enter para continuar...")

def main():
    print("Iniciando programa de Algoritmos de Búsqueda y Ordenamiento...")
    menu_principal()

if __name__ == "__main__":
    main()