import numpy as np
import matplotlib.pyplot as plt
import serial
import time

# Definir el puerto serie al que está conectado el Arduino
puerto_serie = 'COM3'  ##Modificar segun el puerto donde este conectado el arduino

# Inicializar la conexión serial
arduino = serial.Serial(puerto_serie, 9600)  

# Esperar un momento para que se establezca la conexión
time.sleep(2)

# Cargar los vectores del archivo txt
th_1_codo_arriba = np.genfromtxt('th1_euler_abierto.txt', dtype="float")
th_2_codo_arriba = np.genfromtxt('th2_euler_abierto.txt', dtype="float")
##crear vectores donde se almacenaran los datos recibidos
datosr = []
th1r = []
th2r = []
##Variables para calcular ECM
l1 = 104                             
l2 = 181.36
sum_x = 0
sum_y = 0
print("Se ha iniciado el programa...")

##Se intenta hacer la comunicacion con el arduino
try:
    # Bucle para enviar datos al Arduino
    for i in range(min(len(th_1_codo_arriba), len(th_2_codo_arriba))):
        dato1 = th_1_codo_arriba[i]
        dato2 = th_2_codo_arriba[i]
        dato ="{} {}\n".format(dato1, dato2)
        print("Enviando dato: ",dato)
        arduino.write(dato.encode())                            # Enviar los datos al Arduino
        time.sleep(0.2)                                         # Esperar un breve periodo antes de enviar el siguiente conjunto de datos
        
        # Esperar la respuesta del Arduino
        while True:
            respuesta = arduino.readline().decode().strip()     # Leer la respuesta del Arduino
            if respuesta:
                print("Respuesta recibida: ", respuesta,"\n")  # Imprimir la respuesta recibida
                datosr.append(respuesta)
                break                                           # Salir del bucle cuando se reciba la respuesta
            time.sleep(0.2)                                     # Esperar un breve periodo antes de volver a intentar leer la respuesta

    print("\nCerrando la conexión serial...")                  
    time.sleep(0.1)
except KeyboardInterrupt:
    print("\nCerrando la conexión serial...")
    arduino.close()                                             # Cerrar la conexión serial al presionar Ctrl + C

print("Se han recibido los datos correctamente \n")


##Separar los datos en los valores de th1 y th2
for dato_recibido in datosr:
    valores = dato_recibido.split()                             # Separar la línea en dos valores utilizando el espacio como separador
    if len(valores) == 2:                                       # Verificar si se han obtenido dos valores después de separar
        dato1 = float(valores[0])
        dato2 = float(valores[1])
        th1r.append(dato1)
        th2r.append(dato2)
    else:
        print("Error: No se pudieron separar los datos correctamente en la línea:", dato_recibido)

#limpiar datosr para eliminar memoria utilizada
datosr= " "

# Generar el rango de tiempo y total de muestras tomadas
t = np.arange(len(th_1_codo_arriba))
num_puntos = len(th_1_codo_arriba)

##Calcular error cuadratico medio
for i in t:
    x_deseada = l1 * np.cos(th_1_codo_arriba[i]) + l2 * np.cos(th_1_codo_arriba[i] + th_2_codo_arriba[i])
    y_deseada = l1 * np.sin(th_1_codo_arriba[i]) + l2 * np.sin(th_1_codo_arriba[i] + th_2_codo_arriba[i])
    x_obtenida = l1 * np.cos(th1r[i]) + l2 * np.cos(th1r[i] + th2r[i])
    y_obtenida = l1 * np.sin(th1r[i]) + l2 * np.sin(th1r[i] + th2r[i])
    sum_x += sum_x + (x_obtenida - x_deseada)**2
    sum_y += sum_y + (y_obtenida - y_deseada)**2

emc_x = sum_x / num_puntos                                          # EMC en x
emc_y = sum_y / num_puntos                                          # EMC en Y

print("El ECM en X es: ", emc_x)
print("El EMC en Y es: ", emc_y)

print("\nSe estan graficando los resultados...\nEspere unos momentos...\n")
time.sleep(5)

##modificar los limites del eje x para cada figura
#circulo    70
#triangulo  200
#brazo      290

#Graficamos las grficas de las thetas mandadas y recibidas
plt.figure(1)
plt.subplot(1, 2, 1)
plt.title("Gráfica de Thetas enviadas")
plt.plot(t, th_1_codo_arriba)  
plt.plot(t, th_2_codo_arriba)
plt.xlim([-2, 280])  # Ajusta los límites del eje x según sea necesario
plt.ylim([-90, 90])  # Ajusta los límites del eje y según sea necesario
plt.xlabel("Tiempo (t)")
plt.ylabel("Grados (°)")
plt.legend(["Theta 1","Theta 2"])
plt.grid(True)  # Añadir una cuadrícula al gráfico

plt.subplot(1, 2, 2)
plt.title("Gráfica de Thetas recibidas")
plt.plot(t, th1r)  
plt.plot(t, th2r)
plt.xlim([-2, 280])  # Ajusta los límites del eje x según sea necesario
plt.ylim([-90, 90])  # Ajusta los límites del eje y según sea necesario
plt.xlabel("Tiempo (t)")
plt.ylabel("Grados (°)")
plt.legend(["Theta 1","Theta 2"])
plt.grid(True)  # Añadir una cuadrícula al gráfico
plt.show()

