import time
import random

# En esta funcion se realizar la Ordenacion por Insercion
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        valor_actual = lista[i]
        posicion = i - 1

        # Desplaza los elementos mayores al valor_actual a la derecha
        while posicion >= 0 and lista[posicion] > valor_actual:
            lista[posicion + 1] = lista[posicion]
            posicion = posicion - 1

        # Coloca el valor en su lugar correcto
        lista[posicion + 1] = valor_actual


# Esta funcion es por Quick Sort (Ordenación Rápida) ---
def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]

    izquierdos = []
    medios = []
    derechos = []

    for x in lista:
        if x < pivote:
            izquierdos.append(x)
        elif x == pivote:
            medios.append(x)
        else:
            derechos.append(x)

    # Unimos las partes recursivamente
    return quick_sort(izquierdos) + medios + quick_sort(derechos)


# --- PRUEBAS DE TIEMPO (Punto 3 del Taller) ---
tamanos = [10000, 100000]  # Probamos con estos para ver la diferencia

for n in tamanos:
    datos = [random.randint(1, n) for _ in range(n)]

    # Medir Quick Sort
    inicio = time.time()
    _ = quick_sort(datos.copy())
    fin = time.time()
    print(f"Quick Sort (n={n}): {fin - inicio:.4f} segundos")

    # Medir Insertion Sort (Solo para 10,000 porque es lento)
    if n <= 10000:
        inicio = time.time()
        insertion_sort(datos.copy())
        fin = time.time()
        print(f"Insertion Sort (n={n}): {fin - inicio:.4f} segundos")