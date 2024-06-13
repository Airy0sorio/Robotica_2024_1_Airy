import numpy as np
import matplotlib.pyplot as plt
import serial
import time

# Definir el puerto serie al que está conectado el Arduino
puerto_serie = 'COM4'  ##Modificar segun el puerto donde este conectado el arduino

# Inicializar la conexión serial
arduino = serial.Serial(puerto_serie, 9600)  

# Esperar que se establezca la conexión
time.sleep(2)

# Cargar los vectores del archivo txt
th_1 = np.genfromtxt('th1_euler_abierto.txt', dtype="float")
th_2 = np.genfromtxt('th2_euler_abierto.txt', dtype="float")

print("Se ha iniciado el programa...")

##Se intenta hacer la comunicacion con el arduino
try:
    # Bucle para enviar datos al Arduino
    for i in range(min(len(th_1), len(th_2))):
        dato1 = th_1[i]
        dato2 = th_2[i]
        #1 servo
        dato="{}\n".format(dato1)
        #2 servos
        dato="{} {}\n".format(dato1, dato2)
        #print("Enviando dato: ",dato)
        arduino.write(dato.encode())                            # Enviar los datos al Arduino
        print("Dato ",i)
        time.sleep(0.3)                                         # Esperar un breve periodo antes de enviar el siguiente conjunto de datos
        
    print("\nCerrando la conexión serial...")                  
    time.sleep(0.1)
except KeyboardInterrupt:
    print("\nCerrando la conexión serial...")
    arduino.close()                                             # Cerrar la conexión serial al presionar Ctrl + C

print("Se han enviado los datos correctamente \n")

# Generar el rango de tiempo y total de muestras tomadas
t = np.arange(len(th_1))

# Graficamos las graficas de las thetas mandadas
plt.figure(1)
plt.title("Gráfica de Thetas enviadas")
plt.plot(t, th_1)  
plt.plot(t, th_2)
plt.xlim([-2, 90])  # Ajusta los límites del eje x según sea necesario
plt.ylim([-90, 180])  # Ajusta los límites del eje y según sea necesario
plt.xlabel("Tiempo (t)")
plt.ylabel("Grados (°)")
plt.legend(["Theta 1","Theta 2"])
plt.grid(True)  # Añadir una cuadrícula al gráfico

plt.show()
