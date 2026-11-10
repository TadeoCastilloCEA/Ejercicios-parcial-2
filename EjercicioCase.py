nombreArticulo = ""
cantidadArticulo = 0
claveArticulo = ""
categoriaArticulo = ""
precioArticulo = 0

print ("bienvenido al sistema de registro de artículos")
print ("-----------Menu de Registro de Artículos-----------")
print ("1. Registrar un artículo")
print ("2. Ver nombre de artículos registrados")
print ("3. Ver cantidad de artículos registrados")
print ("4. Ver clave de artículos registrados")
print ("5. Ver categoría de artículos registrados")
print ("6. Ver precio de artículos registrados")
print ("7. Salir del sistema de registro de artículos")
print ("---------------------------------------------------")
opcion = int(input("Seleccione la opcion deseada: "))

match opcion:#aqui el match es una validacion de la opcion
    
    case 1:
        nombreArticulo = input("Ingrese el nombre del artículo: ")
        cantidadArticulo = int(input("Ingrese la cantidad del artículo: "))
        claveArticulo = input("Ingrese la clave del artículo: ")
        categoriaArticulo = input ("ingrese la categoría del artículo: ")
        precioArticulo = int(input("Ingrese el precio del artículo: "))
    case 2:
        print ("El nombre del artículo registrado es:", nombreArticulo)
    case 3:
        print ("La cantidad del artículo registrado es:", cantidadArticulo)
    case 4:
        print ("La clave del artículo registrado es:", claveArticulo)
    case 5:
        print ("La categoría del artículo registrado es:", categoriaArticulo)
    case 6:
        print ("El precio del artículo registrado es:", precioArticulo)
    case 7:
        print ("!Hasta luego¡")
        