inventarios=[]
verifi=True
while verifi:
    print("1.agregar producto")
    print("2.mostrar lista de productos")
    print("3.buscar producto por el nombre")
    print("4.actualizar producto")
    print("5.eliminar producto")
    print("6.calcular estadisticas")
    print("7.Guardar CSV")
    print("8.cargar CSV")
    print("9.salir")
    opcion=int(input("que opcion desea? "))
    valortotal=0
    cantidadtotal=0
    preciofinal=0
    preciofinal2=0
    preciofina=0



    if opcion == 1:
        agregarproductonombre=input("dijite el nombre del producto que desea agregar: ")
        agregarproductoprecio=float(input("dijite el precio del producto que desee agregar: "))
        agregarproductocantidad=int(input("dijite la cantidad del producto que desee agregar: "))

        producto = {
            'nombre':agregarproductonombre,
            'precio':agregarproductoprecio,
            'cantidad':agregarproductocantidad
        }
        inventarios.append(producto)


    elif opcion ==2:
        if inventarios==[]:
            print("inventario vacio,recuerda ingresar un producto")

        else:
            for i in inventarios:
                print(f"producto: {i['nombre']} | valor: {i['precio']} | cantidad: {i['cantidad']}")

    elif opcion ==3:
        buscador=input("diga el nombre del producto que esta buscando: ")
        for g in inventarios:
            if buscador == g ['nombre']:
                print(f"producto: {g['nombre']} | valor: {g['precio']} | cantidad: {g['cantidad']}")
            else:
                    print ("producto no encontrado")

    elif opcion ==4:
        encontrado=input("ingrese el producto que desea actualizar: ")
        if inventarios==[]:
            print("inventario vacio,recuerda ingresar un producto")
        else:
            for e in inventarios:
                if encontrado==e['nombre']:
                    namenew=input("dijite el nuevo nombre del producto: ")
                    pricenew=float(input("dijite el nuevo precio del producto: "))
                    cantnew=int(input("dijite la neva cantidad del producto: "))

                    e.update({'nombre':namenew,'precio':pricenew,'cantidad':cantnew})
                else:
                    print ("producto no encontrado")
    
    elif opcion==5:
        eliminado=input("dijite el producto que desee eliminar")
        if inventarios==[]:
            print("inventario vacio,recuerda ingresar un producto")
        else:
            for eli in inventarios:
                if eliminado == eli['nombre']:
                    inventarios.remove(eli)
                else:
                    print ("producto no encontrado")

    elif opcion==6:
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

    elif opcion == 7:
        import csv
        if inventarios == []:
            print("No hay productos para guardar.")
        else:
            with open("login.csv", "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["nombre", "precio", "cantidad"])  # Encabezados
                for prod in inventarios:
                    escritor.writerow([prod["nombre"], prod["precio"], prod["cantidad"]])
            print("Inventario guardado correctamente en login.csv")

    elif opcion == 8:
        import csv
        try:
            with open("login.csv", "r", encoding="utf-8") as archivo:
                lector = csv.reader(archivo)
                next(lector)  # Saltar encabezado
                inventarios.clear()  # Limpiar inventario actual

                for fila in lector:
                    producto = {
                        "nombre": fila[0],
                        "precio": float(fila[1]),
                        "cantidad": int(fila[2])
                    }
                    inventarios.append(producto)

            print("Inventario cargado correctamente desde login.csv")
        except FileNotFoundError:
            print("No se encontró el archivo login.csv")




    if opcion==9:
        verifi = False