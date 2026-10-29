#1 Definición de variables 
nombre_estudiante = "Ramiro" # str (texto) [3]
edad = 22 # int (entero) [3]
promedio=8.5 #float (deicmal) [3]
inscrito=True # Bool (booleano) [3]

#2 mostrar valores en pantalla usando print()
print("Nombre: ", nombre_estudiante) 
print("Edad: ", edad) 
print("Promedio: ",promedio) 
print("Inscrito: ",inscrito) 

num1=7
num2=2
suma=num1+num2
print("La suma de ", num1, " + ", num2, " es: ", suma)
multiplicacion=num1*num2
print("La multiplicación de ", num1, " * ", num2, " es: ", multiplicacion)
potencia=num1**num2
print("La potencia de ", num1, " ** ", num2, " es: ", potencia)

div_float=num1/num2
print("La división de ", num1, " / ", num2, " es: ", div_float)
div_entero=num1//num2
print("La división entera de ", num1, " // ", num2, " es: ", div_entero)
resto=num1%num2
print("El resto de la división de ", num1, " % ", num2, " es: ", resto)

nota_examen=7.5
if nota_examen>=8:
    print("Aprobado con excelencia")
elif nota_examen>=6:
    print("Aprobado")
else:
    print("Desaprobado")

#bucle FOR usando range(inicio,fin)
print("--- conteo del 1 al 1o ---")
for i in range(1,11):
    print("---Número:", i, "---")

#bucle WHILE con variable de control
contador=5
while contador>0:
    print("Cuenta regresiva: ", contador)
    contador=contador-1 #modificamos la variable de control para evitar un bucle infinito

día="lunes"
match día:
    case "lunes":
        print("Hoy es lunes")
    case "martes":
        print("Hoy es martes")
    case "miércoles":
        print("Hoy es miércoles")
    case "jueves":
        print("Hoy es jueves")
    case "viernes":
        print("Hoy es viernes")
    case _:
        print("No es un día válido")

edad=20
tiene_registro=True

if edad>=18 and tiene_registro:
    print("Puede manejar")

# Muestra solo números impares y se detiene si encuentra un 7

for num in range(1, 11):
    if num % 2 == 0:
        continue  # Salta los números pares
    if num == 7:
        print(num)
        break  # Detiene el bucle si encuentra un 7
    

print ("Fin del programa")