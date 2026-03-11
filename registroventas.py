from totalventa import calculototal
from historialventa import historial_ventas
def registerventas():
    is_true = True
    contador = 0
    ventas = {}
    valor = 0

    while is_true :
        contador += 1 
        print("-------------------------------------------")
        nombre_producto = input("Nombre del producto: ")
        precio_unitario = int(input("Precio unitario: "))
        cantidad_vendida = int(input("Cantidad vendida: "))

        ventas[contador] = [nombre_producto, precio_unitario, cantidad_vendida]
    
        nueva_venta = int(input("""Desea ingresar otra venta?:
        1 → SI
        2 → NO 
        digite →  """))
        print("-------------------------------------------")
        cantidad = ventas[contador][2] 
        precio  = ventas[contador][1]
        
        individual_venta = calculototal(cantidad, precio)
        
        valor += individual_venta
        
        if nueva_venta == 2 :
            print("-------------------------------------------")
            historial_ventas(ventas, valor)
            print("-------------------------------------------")
            is_true = False
            
