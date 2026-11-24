"""Definicion de matriz con los datos de inventario y funciones para calcular la cantidad a pedir y generar un informe."""
inventario = [
    [1, "arroz", 2, 3],
    [2, "azucar", 5, 5],
    [3, "sal", 1, 3],
    [4, "frijoles", 2, 1],
    [5, "jabon", 5, 3]
]

"""Determina la cantidad exacta a pedir según el stock mínimo."""
def calcular_pedido(stock_actual, stock_minimo):
    """Si el stock actual es menor que el stock mínimo, devuelve la cantidad a pedir. De lo contrario, devuelve 0."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0

def informe_inventario(inventario):
    """Genera un informe del inventario indicando si se debe pedir más unidades de cada artículo."""
    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        pedir = calcular_pedido(stock_actual, stock_minimo)
        """Si la cantidad a pedir es mayor que 0, se indica que se debe pedir más unidades. De lo contrario, se indica que el stock es suficiente."""
        if pedir > 0:
            print(f"El artículo {nombre} (código {codigo}) tiene un stock actual de {stock_actual}, Se debe pedir {pedir} unidades.")
        else:
            print(f"El artículo {nombre} (código {codigo}) tiene un stock actual de {stock_actual}, que es suficiente. Cantidad a pedir: {pedir} unidades.")

"""Llamada a la función para generar el informe de inventario."""
informe_inventario(inventario)