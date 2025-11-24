def agregar_producto (inventarios,agregarproductonombre,agregarproductoprecio,agregarproductocantidad):
    producto = {
            'nombre':agregarproductonombre,
            'precio':agregarproductoprecio,
            'cantidad':agregarproductocantidad 
        }
    inventarios.append(producto)

def mostrar_inventario(inventarios):
    if inventarios==[]:
            print("inventario vacio,recuerda ingresar un producto")

    else:
        for i in inventarios:
            print(f"producto: {i['nombre']} | valor: {i['precio']} | cantidad: {i['cantidad']}")

def buscar_producto(inventarios,buscador):
    for g in inventarios:
            if buscador == g ['nombre']:
                print(f"producto: {g['nombre']} | valor: {g['precio']} | cantidad: {g['cantidad']}")
            else:
                    print ("producto no encontrado")

def actualizar_producto(inventarios,encontrado,namenew,pricenew,cantnew):
    if inventarios==[]:
            print("inventario vacio,recuerda ingresar un producto")
    else:
        for e in inventarios:
            if encontrado==e['nombre']:


                e.update({'nombre':namenew,'precio':pricenew,'cantidad':cantnew})
            else:
                print ("producto no encontrado")

def eliminar_producto(inventarios,eliminado):
    if inventarios==[]:
        print("inventario vacio,recuerda ingresar un producto")
    else:
        for eli in inventarios:
            if eliminado == eli['nombre']:
                inventarios.remove(eli)
            else:
                print ("producto no encontrado")

def calcular_estadisticas(inventarios):
    valortotal=0
    cantidadtotal=0
    preciofinal=0
    preciofinal2=0
    preciofina=0
    estadistica=input("ingrese el nombre del producto al que le quiere sacar el valor total del inventario o si los quiere todos: ")
    if inventarios==[]:
        print("inventario vacio,recuerda ingresar un producto")
    else:
        for esta in inventarios:
            if estadistica == esta['nombre']:
                valortotal=esta['precio']
                cantidadtotal=esta['cantidad']
                preciofinal=valortotal*cantidadtotal
                print(f"producto: {esta['nombre']} | valor: {esta['precio']} | cantidad: {esta['cantidad']} | su valor total es {preciofinal}")
            elif estadistica=="todos":
                    preciofina= esta['cantidad']*esta['precio']
                    preciofinal2+=preciofina
                    cantidadtotal+=esta['cantidad']
            maximovalor=None
            maximocantidad=None
            nameva=""
            nameca=""
            for maxi in inventarios:
                if maximovalor is None or maxi['precio']>maximovalor:
                    maximovalor=maxi['precio']
                    nameva=maxi['nombre']
                if maximocantidad is None or maxi ['cantidad']>maximocantidad:
                        maximocantidad=maxi['cantidad'] 
                        nameca=maxi['nombre']

        print(f"hay un total de {cantidadtotal} de productos, y en total con todos los productos tienes {preciofinal2} a la venta")
        print(f"el producto con mayor precio es: {nameva} | valor: {maximovalor} ")
        print(f"el producto con mayor cantidad es: {nameca} | cantidad: {maximocantidad} ")
