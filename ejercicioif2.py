nombre = ""
edad = 0
nacionalidad = ""

nombre = input ("Ingrese su nombre: ")
edad = int (input ("Ingrese su edad: "))
nacionalidad = input ("Ingrese su nacionalidad: ")

if edad >= 18: #el if va seguido de la condicion y dos puntos
    print ("Esta persona es mayor de edad")
else: #el else va seguido de dos puntos 
    print ("Esta persona no es mayor de edad") 

if nacionalidad == "N": #el if va seguido de la condicion y dos puntos
    print ("Esta persona es de nacionalidad mexicana")
else: #el else va seguido de dos puntos
    print ("Esta persona no es de nacionalidad mexicana")