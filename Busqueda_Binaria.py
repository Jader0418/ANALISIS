import time

def busqueda_binaria(lista, objetivo):

    inicio = 0
    fin = len(lista) - 1
    pasos = 0

    while inicio <= fin:
        pasos += 1
        medio = (inicio + fin) // 2

        if lista[medio] == objetivo:
            return medio, pasos
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1, pasos
# Aca se realiza la prueba empirica.
def realizar_prueba(n):
    # Crear lista ordenada de tamaño n
    datos = list(range(n))
    objetivo = n - 1  # Se hace la busqueda del Peor Caso.

    inicio_t = time.time()
    posicion, total_pasos = busqueda_binaria(datos, objetivo)
    fin_t = time.time()

    print(f"Tamaño de lista (n): {n}")
    print(f"Posición encontrada: {posicion}")
    print(f"Pasos realizados: {total_pasos}")
    print(f"Tiempo de ejecución: {fin_t - inicio_t:.8f} segundos")
    print("-" * 30)

realizar_prueba(1000)
realizar_prueba(100000)
realizar_prueba(1000000)