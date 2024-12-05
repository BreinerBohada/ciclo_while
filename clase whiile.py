#ciclo while

#whil condicion:
#bloque de codigo a repetir
#definir una variable q lleve el control del ciclo

#numero = 1
#while numero <= 5: #cpndicion para iterar n veces
#print(numero)
#numero +=1


# numero = 10

# while numero >=1: 
#     print (numero)
#numero -=1

#crear un programa que sume los numeros ingresados por el usuario hasta que el usuario ingrese zero

# suma =0
# number = int(input("ingresa un numero o pulsa 0 para salir: "))

# while number !=0:
#     suma += number
#     number = int(input("ingresa un numero o pulsa 0 para salir: "))

# print  (f"la suma total de los numeros es de: {suma}")


#condiciones dinamicas:
#son aleatorias, y pueden cambiar con la ejecucion de un codigo

#simulacion basada en una condicion externa
#simularemos el crecimiento de una poblacion hasta que alcance un limite

# poblacion = 1000

# limite = 5000
# tasacrec = 1.1
# anio = 1

# while poblacion < limite:
#     print (f"En el año {anio}, poblacion actual: {poblacion}")
#     poblacion = int(poblacion * tasacrec)
#     anio +=1

# print (f"poblacion final alcanzada: {poblacion}")

#lecturas de un sensor 
# simular la lectura de un sensor que medira valores aleatorios hasta que alcance un valor objetivo

# import random

# sensor = random.randint(0, 80)
# objetivo = 80
# cont = 1

# while sensor < objetivo:
#     print (f"en la lectura numero {cont}, el valor del sensor es de: {sensor}")
#     sensor +=random.randint(1, 10)
#     cont +=1

# print (f"la lectura final alcanzada fue de: {sensor}")


#