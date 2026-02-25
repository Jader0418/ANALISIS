import time
import random
import sys

# El limite de recursion es alto, por si la lista llega a ser grande.
sys.setrecursionlimit(2000000)


def ordenar_quicksort(lista):
    # Si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]

    # Creamos las tres sublistas
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    # Se usa recursividad para unirlos a todos.
    return ordenar_quicksort(menores) + iguales + ordenar_quicksort(mayores)

n = 100000
datos = [random.randint(1, n) for _ in range(n)]

print(f"Iniciando Quick Sort para {n} elementos...")
inicio = time.time()
datos_ordenados = ordenar_quicksort(datos)
fin = time.time()

print(f"Tiempo final de Quick Sort: {fin - inicio:.4f} segundos.")