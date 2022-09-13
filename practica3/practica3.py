#1
'''
def empieza_con(letra,archivo):
    suma = 0
    with open (archivo, 'r') as arch:
        #as es como decirle q lo voy a usar abajo 
        for line in arch:
            if line[0].upper() != str(letra).upper():
                suma += 1
    print ('La cantidad de lineas del archivo que no empiezan con',letra, "es",suma)
    
empieza_con("e", "manipulacion1.txt")
'''
#2
'''
def leer_n_lineas(archivo, lineas):
     variable = open(archivo, "r").readlines()[:lineas+1]
     print(*variable)
     
leer_n_lineas("hola.txt", 3)
'''
#3
'''def leer_escribir_primera_linea(archivo, cantidad_de_archivos):
    linea = open(archivo,"r").readlines()[-cantidad_de_archivos:]
    print(*linea)
    
leer_escribir_primera_linea("hola.txt",3)'''

#4
'''
def leer_archivo(archivo):
    linea = open(archivo,"r").read()
    print("Tiene",len(linea.split()),"palabras :)")
leer_archivo("hola.txt")
'''
#5
'''
def reemplazar (arch1, arch2, letra):
    with open(arch1, "r") as file, open(arch2, "w") as file2:
        for line in file:
            file2.write(line.replace(letra, letra + "\n"))

reemplazar("hola.txt", "hola2.txt", "h")'''
   
#6
'''
def sacar_salto(arch1, arch2):
    with open(arch1, 'r') as file, open(arch2, 'w') as file2:
        variable = file.read()
        for elem in variable:
                if elem == '\n':
                    pass
                else:
                    file2.write(elem)

sacar_salto('hola.txt', 'hola2.txt')
'''

#7
'''
def palabra_larga(archivo):
    file = open(archivo,"r")
    leer = file.read()
    dividir = leer.split()
    final = ""
    for palabra in dividir :
        if len(palabra) > len(final):
            final = palabra
    print("la palabra mas larga es", final, "con", len(final), "letras")
'''    

#8
'''
def agrupar(archivo1, archivo2, archivo3):
    with open(archivo1, 'r') as file, open(archivo2, 'r') as file2, open(archivo3, 'w') as file3:
        file3.write("archivo1 \n")
        file3.write(file.read())
        file3.write("\n \n archivo2 \n")
        file3.write(file2.read())

agrupar('hola.txt','hola2.txt','hola3.txt')
'''

#9
'''
def frecuencia(archivo):
    with open(archivo, 'r') as file:
        palabras = file.read()
        lista = palabras.split()
        dic = {}
        for palabra in lista:
            dic[palabra]=int(lista.count(palabra)) / int(len(lista))
        print(dic)

frecuencia('hola.txt')
'''

#10
'''
import os
import glob

def unir_txt(carpeta1, nombre):
    os.chdir(carpeta1)
    textos = glob.glob('*.txt')
    os.mkdir('Resuelto')
    with open('Resuelto/' + nombre, 'a') as salida:
        for archivo in textos:
            with open(archivo, 'r') as texto:
                salida.write(texto.read() + '\n')
unir_txt('ej10', 'salida.txt')
'''

