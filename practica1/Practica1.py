#1
palabra = input("Palabra que quieras saber cauntas letras tiene:  ")
print(len(palabra))

#2
palabra = input("Escribi la palabra: ")
print(palabra[4:6].upper())

#3
nombre = input ("Nombre y Apellido: ")
print ("Hola", nombre)

#4
nombre = input ("nombre: ")
apellido = input ("appelido: ")
print("hola", (nombre[0:1].upper()), (apellido[0:1].upper()))

#5
num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))
num3 = int(input("numero 3: "))
print ((num1 + num2 + num3) / 3 )

#6
hora = int(input("ingresa hora"))
print (hora // 60, "horas y", hora % 60, "minutos") 

#7
venta1= int(input('dinero primera venta:  $'))
venta2= int(input('dinero segunda venta:  $'))
venta3= int(input('dinero tercera venta:  $'))
venta4= int(input('dinero cuarta venta:  $'))
print ('Comisiones totales = ', (venta1+venta2+venta3+venta4)/10 ,'Sueldo total', abs(((venta1+venta2+venta3+venta4)/10)+ 1000))

#8
aprobado = int(input('Respuestas correctas: '))
desaprobado = int(input('Respuestas incorrectas: '))
blanco = int(input('Respuestas en blanco: '))
print ("Nota final",((aprobado*4 + desaprobado* -1) * 100 / ((aprobado+desaprobado+blanco)*4)),"%")

#9

valor_total = int(input("costo de la casa: "))
porcentaje_deposito = valor_total* 0.25
cantidad_ahorrada = 0
inversion_mensual = 0.04/12
sueldo_anual = int(input("sueldo anual: "))
porcentaje_ahorrado = float(input("porcentaje a ahorrar: "))
sueldo_mensual = sueldo_anual/12
contador = 0
while True:
    
    if cantidad_ahorrada<porcentaje_deposito:
        cantidad_ahorrada += (sueldo_mensual*porcentaje_ahorrado+sueldo_mensual*inversion_mensual)
        contador += 1
    else:
        break
    
print("Va a tardar",contador, "meses en ahorrar el depositio")