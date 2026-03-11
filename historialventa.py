def historial_ventas(ventas, valor):
    print("\nRESUMEN DE VENTAS DEL DÍA")
    print()
    
    for producto in ventas.values():
        print(f"Producto: {producto[0]}")
        print(f"Cantidad total vendida: {producto[2]}")
        print()
    
    print(f"Total recaudado: ${valor}")