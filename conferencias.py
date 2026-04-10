def seleccion_actividades(actividades):
    # ORDENAR LAS ACTIVIDADES POR SU HORA DE FIN
    actividades.sort(key=lambda x: x[1])
    
    seleccionadas = []
    
    # SELECCIONAR LA PRIMERA ACTIVIDAD
    seleccionadas.append(actividades[0])
    ultima_fin = actividades[0][1]
    
    # RECORRER LAS ACTIVIDADES RESTANTES
    for i in range(1, len(actividades)):
        inicio, fin = actividades[i]
        
        if inicio >= ultima_fin:
            seleccionadas.append(actividades[i])
            ultima_fin = fin
    
    return seleccionadas


actividades = [
    (8.0, 9.0),   # CONFERENCIA 1
    (8.5, 10.0),  # CONFERENCIA 2
    (9.0, 10.0),  # CONFERENCIA 3
    (10.0, 11.0), # CONFERENCIA 4
    (9.5, 11.5),  # CONFERENCIA 5
    (11.0, 12.0)  # CONFERENCIA 6
]

resultado = seleccion_actividades(actividades)

print("Actividades seleccionadas:")
for act in resultado:
    print(act)
    
    
    
    