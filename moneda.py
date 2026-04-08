def cambio_voraz(monedas, monto):
    resultado = {}
    
    for moneda in monedas:
        cantidad = monto // moneda  # cuántas monedas usar
        if cantidad > 0:
            resultado[moneda] = cantidad
            monto = monto % moneda  # lo que sobra
    
    return resultado


# Datos del problema
monedas = [100, 50, 20, 10, 5, 1]
monto = 289

resultado = cambio_voraz(monedas, monto)

# Mostrar resultado
print("Desglose de monedas:")
total_monedas = 0

for moneda in resultado:
    print(f"{moneda}: {resultado[moneda]}")
    total_monedas += resultado[moneda]

print("Total de monedas:", total_monedas)