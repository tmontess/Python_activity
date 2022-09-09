#6 da vuelta la lista ingresada por teclado
'''
lista1 = []
for elementos in range(5):
    lista1.append(input("dame una palabra:  "))
lista2 = list(lista1)
lista2.reverse()

for elemento in lista2:
    print (elemento)
'''
# 7

'''Creá un programa que declare una lista y la vaya llenando de números leídos por teclado 
hasta que se introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.'''


#Ejercicio 8
'''
Realizá un programa que declare tres listas lista1, lista2 y lista3, donde las dos primeras listas deben
tener cinco enteros cada una, ingresados por teclado y asigne para cada elemento de la lista3 la suma de
los elementos de la lista1 y la lista2 (es decir, el primer elemento de la lista3 tiene que ser la suma del 
primer elemento de la lista1 y el primero de la lista2)

'''
'''
lista1 = [
    int(input("ingresar numero 1a: ")),
    int(input("ingresar numero 2a: ")),
    int(input("ingresar numero 3a: ")),
    int(input("ingresar numero 4a: ")),
    int(input("ingresar numero 5a: ")),]
lista2 = [
    int(input("ingresar numero 1b: ")),
    int(input("ingresar numero 2b: ")),
    int(input("ingresar numero 3b: ")),
    int(input("ingresar numero 4b: ")),
    int(input("ingresar numero 5b: ")),]
lista3 = []
lista3.append(lista1[0] + lista2[0])
lista3.append(lista1[1] + lista2[1])
lista3.append(lista1[2] + lista2[2])
lista3.append(lista1[3] + lista2[3])
lista3.append(lista1[4] + lista2[4])

print(lista3)
'''
#Ejercicio 9
'''
Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. 
Se debe introducir el nombre y la edad de cada alumno por teclado. 
El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). 
Al finalizar se deben mostrar los siguientes datos:

La edad máxima de todos los alumnos.
Los alumnos que tengan la edad máxima
'''
'''
nombre_edad = {}
print("Nombre y edad de los alumnos. Escriba * para finalizar")
while True:
    nombre_apellido = input("Nombre y apellido: ")
    edad= input("Edad: ")
    if nombre_apellido != "*":
        nombre_edad[nombre_apellido]= edad
        
    else:
        break
edad_maxima = 0
for nombre in nombre_edad:
    if int(nombre_edad[nombre_apellido]) > int(edad_maxima):
        edad_maxima = nombre_edad[nombre]
        
print("la edad maxima es de", edad_maxima, "años, y es", nombre )'''

#Ejercicio 10
'''
Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la
cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el 
carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).
'''
'''
dic= {}
palabra = input("Cuantos caracteres tiene: ")
for lista in palabra:
    dic[lista]=0
for listas in palabra:
    dic[listas]= dic[listas] + 1 
print(dic)
'''

#12
'''Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido.
Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán 
los nombres de los alumnos y los valores serán listas con las notas de cada alumno. El programa tiene que pedir 
el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo.
Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. 
Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.'''

'''
dic= {}
print(int(input("Cantidad de alumnos para cargar: ")))
while True:
    print("coloque * para finalizar")
    nombre_appelido= input("Nommbre y apellido del alumno: ")
    if nombre_appelido != "*":
        while True:
            print("Escriba -1 para pasar al siguiente alumno: ")
            nota= int(input("Notas: "))
            if nota >= 0:
                if nombre_appelido not in dic:
                    dic[nombre_appelido]=[nota]
                else:
                    dic[nombre_appelido].append(nota)
            else:
                break
    else:
        break
final = {}
for nombre_appelido in dic:
    final[nombre_appelido]= (sum(dic[nombre_appelido])/len(dic[nombre_appelido]))
print(final)

'''

#Ejercicio 13

#Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función esMultiplo.
'''
def es_multiplo (num1, num2):
    if num1 / num2 == int(num1/num2) or num2 / num1 == int(num2/num1): 
        print("son multiplos")
    else:
        print("no son multiplos")
'''
# Ejercicio 14
'''
def tmp_promedio(max, min):
    print("temperatura promedio",(max+min)/2,"grados")

dias=int(input("cantidad de dias: "))
contador = 0
for dia in range(dias):
    if contador < dias:
        maxima = int(input("Temp. max: "))
        minima = int(input("Temp. min: "))
        tmp_promedio(maxima,minima)
        contador =+ 1
print("Espero que te sirva")
'''
#Ejrcicio 15
'''Creá un programa para gestionar datos de los socios de un club, el cual permita:

Cargar la información de los socios en un diccionario para acceder por número de socio. 
Los datos que se deben almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), 
cuota al dia (s/n) (el programa tiene que dejar de cargar cuando se ingrese el número 0). 
El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día
Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día
Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día
Informar la cantidad de socios que tiene el club.
Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.
Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.
Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
Imprimir el listado de socios completos.
Definir las funciones que creas necesarias.'''

from pickletools import int4
from time import process_time_ns


dic={
1:["Florencia Ocampo", "14/09/2001", "si"],

2:["David Estévez", "14/09/2001", "si"],

3:["Sofía Cáceres", "14/09/2001", "si"]
}
while True:
    print("cargar numero de socio, para finalizar colocar 0 ")
    numero_socio= int(input("Numero de socio: "))
    if numero_socio != 0:
        nombre_appelido= input("Nombre y apellido: ")
        fecha= input("Fecha de ingreso: ")
        cuota= input("Cuota al dia si/no: ")
        dic[numero_socio]=[nombre_appelido,fecha,cuota]
    else:
        break
print("El club tine",len(dic),"socios")
    
verificar = input("¿Verificar cuotas de socios? si/no: ")
if verificar.upper() == "SI":
    while True:
        print("Introduzca 0 para finalizar")
        socio=int(input("Numero del socio: "))
        if socio != 0:
            if socio not in dic:
                print("Este socio no existe")
            else: 
                if dic[socio][-1].upper() == "SI":
                    print("El",dic[socio][0],"esta al dia")
                else:
                    print("El",dic[socio][0],"no esta al dia")
                    
        else:
            break
else:
    pass

dic_copy={}

eliminar = input("Eliminar socio si/no: ")
if eliminar.upper() == "SI":
    while True:
        print("Para finalizar coloque 0")
        elim= input("Numero del socio: ")
        if elim != "0":
            for elemento in dic:
                if elim.upper() != dic[elemento][0].upper():
                    dic_copy[elemento]=dic[elemento]
            
            else:
                break       
else:
    pass
dic = dic_copy

cambiar = input("Cambiar fecha socios si/no: ")
if cambiar.upper() == "SI":
    while True:
        print("Para terminar, ingresa 0")
        elim = input("fecha a cambiar: ")
        if elim != "0":
            fecha_nueva= input("nueva fecha: ")
            for elemento in dic:
                if dic[elemento][1] == elim:
                    dic[elemento][1]=fecha_nueva
        else:
            break
else:
    pass

print(dic)