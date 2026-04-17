def mochila_voraz_personalizada(elementos, capacidad_max):
    # Se crea una lista de diccionarios para representar cada objeto
    # con su id, peso y beneficio de forma más legible
    objetos = []
    for i, (peso, beneficio) in enumerate(elementos):
        # enumerate da el índice i y desempaqueta la tupla (peso, beneficio)
        objetos.append({
            'id': i + 1,          # id empieza en 1, no en 0
            'peso': peso, 
            'beneficio': beneficio
        })

# ⚠️ PROBLEMA AQUÍ: ordena por peso ascendente (menor peso primero)
    # Esto NO es el criterio correcto para mochila fraccionaria
    # El criterio correcto sería ordenar por beneficio/peso DESCENDENTE:
    # objetos.sort(key=lambda x: x['beneficio'] / x['peso'], reverse=True)
    objetos.sort(key=lambda x: x['peso'])
    
    beneficio_total = 0   # acumula el beneficio de los objetos seleccionados
    peso_actual = 0       # acumula el peso ocupado en la mochila
    seleccionados = []    # guarda los objetos que sí entraron

    for obj in objetos:
        # Verifica si el objeto cabe completamente en la mochila
        if peso_actual + obj['peso'] <= capacidad_max:
            # Si cabe, se toma completo (lógica 0-1, no fraccionaria)
            peso_actual    += obj['peso']
            beneficio_total += obj['beneficio']
            seleccionados.append(obj)
        else:
            # ⚠️ PROBLEMA: solo imprime que no cabe, pero en mochila
            # fraccionaria debería tomar la fracción disponible así:
            #
            # espacio_restante = capacidad_max - peso_actual
            # fraccion = espacio_restante / obj['peso']
            # beneficio_total += fraccion * obj['beneficio']
            # peso_actual += espacio_restante
            print(f"Objeto {obj['id']:<3}  | {obj['peso']:<6} | (No cabe)")
            
datos_objetos = [(10, 20), (20, 30), (30, 66), (40, 40), (50, 60)]
# Cada tupla es (peso, beneficio)
# Objeto 1: peso=10, beneficio=20  → densidad = 2.0
# Objeto 2: peso=20, beneficio=30  → densidad = 1.5
# Objeto 3: peso=30, beneficio=66  → densidad = 2.2  ← debería ir primero
# Objeto 4: peso=40, beneficio=40  → densidad = 1.0
# Objeto 5: peso=50, beneficio=60  → densidad = 1.2

capacidad = 100
total_b, total_p = mochila_voraz_personalizada(datos_objetos, capacidad)
print(f"BENEFICIO TOTAL: {total_b}")