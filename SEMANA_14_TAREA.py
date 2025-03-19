 #Código creado por Jeison Teobaldo Garcia Arreaga
 #Parámetros y retorno de valores en funciones

def obtener_descuento(total_compra, porcentaje_desc=15):
    # Se calcula el valor del descuento
    valor_descuento = total_compra * (porcentaje_desc / 100)
    return valor_descuento


def mostrar_detalles(compra, porcentaje_desc=15):
    # Se determina el descuento y el monto final
    valor_descuento = obtener_descuento(compra, porcentaje_desc)
    total_a_pagar = compra - valor_descuento
    # Se presentan los detalles de la compra
    print("========== Detalles de la Compra ==========")
    print(f"Valor Total de la Compra: ${compra:.2f}")
    print(f"Descuento Aplicado ({porcentaje_desc}%): ${valor_descuento:.2f}")
    print(f"Total a Pagar: ${total_a_pagar:.2f}")
    print("===========================================")


def ejecutar():
    print("Sistema de Descuentos - Jeison Garcia Arreaga\n")

    # Primera compra con descuento predeterminado
    total_1 = 1500
    mostrar_detalles(total_1)

    # Segunda compra con un porcentaje de descuento distinto
    total_2 = 750
    porcentaje_2 = 25
    mostrar_detalles(total_2, porcentaje_2)


if __name__ == "__main__":
    ejecutar()