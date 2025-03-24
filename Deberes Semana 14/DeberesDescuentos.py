# Deberes Johanna

# ejemplo, descuento

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """Calcula el descuento y el monto final a pagar."""
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final

# Llamadas a la función con diferentes valores
monto1 = 150
descuento1, total1 = calcular_descuento(monto1)

monto2 = 300
descuento2, total2 = calcular_descuento(monto2, 20)

# Mostrar resultados
print(f"Compra 1 - Total: ${monto1}, Descuento: ${descuento1:.2f}, Total a pagar: ${total1:.2f}")
print(f"Compra 2 - Total: ${monto2}, Descuento: ${descuento2:.2f}, Total a pagar: ${total2:.2f}")
