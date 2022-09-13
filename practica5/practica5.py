#1

'''
lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super + "arroz"
except TypeError:
    print("no puedo agregar arroz")
    '''
#cuando hagamos except hay q saber q tipo de error buscamos 

#2
'''
Definir una función que tenga como parámetros una lista de números por un lado y un
número por otro y devuelva una lista con la división de cada elemento por el número dado.
Por ejemplo, si le paso ([2,4,6,8], 2), debería retornar [1,2,3,4]. Tomar las precauciones necesarias.
''''''
try:
    def division(lista, numero):
        list= []
        for num in lista:
            list.append(num/numero)
        print(list)
    division([2,4,6,8], 0)
except ZeroDivisionError:
    print("No se puede dividir por cero")
except:
    print("Otro error")
'''

#3
'''
Definir un procedimiento, que reciba una lista y un número, el cual tiene que agregar el número 
a la lista solo si el número es positivo. De lo contrario debería generar un error indicando que 
el número no es positivo.
'''
try:
    list = []
    while True:
        print("Ingresa los numeros de la lista, escriba 000 para finalizar la lista")
        lista = int(input("introducir numero de lista: "))

        if lista != 000:
            list.append(lista)
        else:
            break

    num = int(input("introducir numero: "))
    if num >= 0 :
        list.append(num)
        print(list)
except ValueError:
    print("El numero es negativo")