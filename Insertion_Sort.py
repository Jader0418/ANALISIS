import time
import random


def ordenar_insercion(lista):
    # Recorremos la lista desde el segundo elemento
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1

        # Comparamos y desplazamos los elementos hacia la derecha
        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = valor


#Prueba Empirica
n = 10000 #Solo para 10k, para que la computadora no se vaya a bloquear
datos = [random.randint(1, n) for _ in range(n)]

print(f"Iniciando Inserción para {n} elementos...")
inicio = time.time()
ordenar_insercion(datos)
fin = time.time()

print(f"Tiempo final de Inserción: {fin - inicio:.4f} segundos.")