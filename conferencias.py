def seleccion_actividades(actividades):
    # ordenar por tiempo de finalización
    actividades.sort(key=lambda x: x[2])
    
    seleccionadas = []
    
    # tomar la primera
    seleccionadas.append(actividades[0])
    ultima_fin = actividades[0][2]
    
    # recorrer las demás
    for i in range(1, len(actividades)):
        nombre, inicio, fin = actividades[i]
        
        if inicio >= ultima_fin:
            seleccionadas.append(actividades[i])
            ultima_fin = fin
    
    return seleccionadas


# Datos (con nombres)
actividades = [
    ("Conferencia 1", 8.0, 9.0),
    ("Conferencia 2", 8.5, 10.0),
    ("Conferencia 3", 9.0, 10.0),
    ("Conferencia 4", 10.0, 11.0),
    ("Conferencia 5", 9.5, 11.5),
    ("Conferencia 6", 11.0, 12.0)
]

resultado = seleccion_actividades(actividades)

print("Actividades seleccionadas:\n")

for nombre, inicio, fin in resultado:
    print(f"{nombre} → Inicio: {inicio} | Fin: {fin}")