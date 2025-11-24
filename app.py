import servicios
import archivos

inventarios=[]


while True:
    print("1.agregar producto")
    print("2.mostrar lista de productos")
    print("3.buscar producto por el nombre")
    print("4.actualizar producto")
    print("5.eliminar producto")
    print("6.calcular estadisticas")
    print("7.Guardar CSV")
    print("8.cargar CSV")
    print("9.salir")


    try:
        opcion=int(input("que opcion desea? "))
        if opcion<0 and opcion>9:
            print("error, solo numeros del 1 al 9")
        else:
            match opcion:
                case 1:
                    agregarproductonombre=input("dijite el nombre del producto que desea agregar: ")
                    agregarproductoprecio=float(input("dijite el precio del producto que desee agregar: "))
                    agregarproductocantidad=int(input("dijite la cantidad del producto que desee agregar: "))

                    servicios.agregar_producto(inventarios,agregarproductonombre,agregarproductoprecio,agregarproductocantidad)

                case 2:
                    servicios.mostrar_inventario(inventarios)

                case 3:
                    buscador=input("diga el nombre del producto que esta buscando: ")
                    servicios.buscar_producto(inventarios,buscador)

                case 4:
                    encontrado=input("ingrese el producto que desea actualizar: ")
                    namenew=input("dijite el nuevo nombre del producto: ")
                    pricenew=float(input("dijite el nuevo precio del producto: "))
                    cantnew=int(input("dijite la neva cantidad del producto: "))
                    servicios.actualizar_producto(inventarios,encontrado,namenew,pricenew,cantnew)

                case 5:
                    eliminado=input("dijite el producto que desee eliminar")
                    servicios.eliminar_producto(inventarios,eliminado)

                case 6:
                    servicios.calcular_estadisticas(inventarios)

                case 7:
                    archivos.guardar_csv(inventarios,filename='inventario.csv')

                case 8:
                    inventarios[:] = archivos.cargar_csv()


                case 9:
                    break
    except ValueError:
        print("ingrese un valor correcto,intente de nuevo")
