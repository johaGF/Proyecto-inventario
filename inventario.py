# Curso: Fundamentos de Programación (213022)
# Fase 5 - Evaluación Final POA
# Solución al Problema 3: Auditoría de Inventario y Reabastecimiento

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Función (módulo) para determinar la cantidad exacta a pedir para un artículo.
    Aplica la lógica de negocio requerida.
    """
    if stock_actual < stock_minimo:
        # Si el stock actual es menor al mínimo, se pide la diferencia
        cantidad_a_pedir = stock_minimo - stock_actual
    else:
        # Si hay suficiente stock, la cantidad a pedir es cero
        cantidad_a_pedir = 0
        
    return cantidad_a_pedir


def main():
    # 1. Crear la matriz con al menos 5 artículos.
    # Formato de cada fila: [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]
    inventario = [
        ["A001", "Cuadernos", 15, 30],
        ["A002", "Bolígrafos", 50, 40],
        ["A003", "Marcadores", 8, 25],
        ["A004", "Resmas de Papel", 12, 12],
        ["A005", "Calculadoras", 3, 10]
    ]
    
    print("=" * 50)
    print("   REPORTE DE AUDITORÍA Y PEDIDOS DE INVENTARIO   ")
    print("=" * 50)
    print(f"{'Artículo':<20} | {'Cantidad a Solicitar'}")
    print("-" * 50)
    
    # 2. Recorrer la matriz y procesar cada artículo
    for articulo in inventario:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        # Llamar al módulo para calcular la cantidad
        pedido_exacto = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        # 3. Salida: Imprimir la lista de pedidos
        print(f"{nombre:<20} | {pedido_exacto}")
        
    print("=" * 50)

# Ejecutar el programa principal
if __name__ == "__main__":
    main()