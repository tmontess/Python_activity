'''Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no 
empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").'''
#1

def empieza_con(letra,archivo):
    suma = 0
    with open (archivo, 'r') as file:
        #as es como decirle q lo voy a usar abajo 
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                suma += 1
    print ('La cantidad de lineas del archivo que no empiezan con',letra, "es",suma)
    
empieza_con("e", "manipulacion1.txt")
''
#2
'''Escribí un programa que lea un archivo e imprima las primeras n líneas.'''

'''def leer_escribir_primera_linea(archivo, cantidad_de_archivos):
    linea = open("manipulacion1.txt","r").readline()[:cantidad_de_archivos]
    print(*linea)
    
leer_escribir_primera_linea("manipulacion1.txt",2)
'''
#3
'''Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y
luego imprima las n últimas.
'''

'''def leer_escribir_primera_linea(archivo, cantidad_de_archivos):
    linea = open("manipulacion1.txt","r").readlines()[-cantidad_de_archivos:]
    print(*linea)
    
leer_escribir_primera_linea("manipulacion1.txt",3)
'''
#4
''