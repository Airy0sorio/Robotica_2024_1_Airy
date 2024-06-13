import numpy as np
import matplotlib.pyplot as plt
import os

def clear_console():
    #para windows
        _ = os.system('cls')
np.set_printoptions(precision=3)
clear_console()

# Valores conocidos
t = np.arange(-6, 361, 3)             #Vector tiempo
l1 = 104                              #Valor del eslabon 1
#l2 = 146                              #Valor del eslabon 2
l2 = 181.36
Px = 250 - 35 * np.cos(np.radians(t)) #Funcion que se desea dibujar en x
Py = 0 - 35 * np.sin(np.radians(t))   #Funcion que se desea dibujar en y

tam = len(Px)
th_1_codo_arriba = np.zeros(tam)  # Matriz para almacenar th_1
th_2_codo_arriba = np.zeros(tam)  # Matriz para almacenar th_2
th_1_codo_abajo = np.zeros(tam)  # Matriz para almacenar th_1
th_2_codo_abajo = np.zeros(tam)  # Matriz para almacenar th_2
for j in range(1):  # For de repeticiones
    plt.pause(5)
    for i in range(tam): 
        # 1era sustitucion
        u = l1 ** 2 + Px[i] ** 2 + Py[i] ** 2 - l2 ** 2
        v = -2 * l1 * Px[i]
        w = -2 * l1 * Py[i]

        # 2da sustitucion
        a = u - v  # cuadrado
        b = 2 * w  # lineal
        c = u + v  # cte

        # codo arriba
        th_11 = 2 * np.arctan2((-b + np.sqrt(b ** 2 - 4 * a * c)) , (2 * a))
        th_2a = np.arctan2((Py-l1*np.sin(th_11)),(Px-l1*np.cos(th_11)))
        th_12=th_2a[i]-th_11
        x11 = l1 * np.cos(th_11)
        y11 = l1 * np.sin(th_11)
        x12 = l1 * np.cos(th_11) + l2 * np.cos(th_11+th_12)
        y12 = l1 * np.sin(th_11) + l2 * np.sin(th_11+ th_12)

        th_1_codo_arriba[i] = th_11  # Almacena el valor de th_1
        th_2_codo_arriba[i] = th_12  # Almacena el valor de th_2


        # # codo abajo
        th_21 = 2 * np.arctan2((-b - np.sqrt(b ** 2 - 4 * a * c)) , (2 * a))
        th_2b = np.arctan2((Py-l1*np.sin(th_21)),(Px-l1*np.cos(th_21)))
        th_22=th_2b[i]-th_21
        x21 = l1 * np.cos(th_21)
        y21 = l1 * np.sin(th_21)
        x22 = l1 * np.cos(th_21) + l2 * np.cos(th_21+th_22)
        y22 = l1 * np.sin(th_21) + l2 * np.sin(th_21+th_22)

        th_1_codo_abajo[i] = th_21  # Almacena el valor de th_1
        th_2_codo_abajo[i] = th_22  # Almacena el valor de th_2

        plt.figure(1)
        plt.clf()  # Limpiar la figura

        #grafico codo arriba
        plt.subplot(1, 2, 1)
        plt.title("Codo arriba")
        plt.plot(Px, Py)
        plt.plot([0, x11], [0, y11], 'rd-')
        plt.plot([x11, x12], [y11, y12], 'bd-')
        plt.xlim([-10, 300])
        plt.ylim([-50, 100])
        plt.legend(["Curva de movimiento", "l1", "l2"])
        plt.grid(True)
        # grafico codo abajo
        plt.subplot(1, 2, 2)
        plt.title("Codo abajo")
        plt.plot(Px, Py)
        plt.plot([0, x21], [0, y21], 'rd-')
        plt.plot([x21, x22], [y21, y22], 'bd-')
        plt.xlim([-10, 300])
        plt.ylim([-100, 50])
        plt.legend(["Curva de movimiento", "l1", "l2"])
        plt.grid(True)
        plt.show(block=False)
        plt.pause(0.05)

# Para almacenarlo en un archivo txt puedes usar:
np.savetxt('th1_C.txt',  np.degrees(th_1_codo_arriba), fmt='%f')
np.savetxt('th2_C.txt',  np.degrees(th_2_codo_arriba), fmt='%f')

plt.figure(2)
plt.subplot(1, 2, 1)
plt.title("Graficas de Thetas para codo arriba")
plt.plot(t[:tam], np.degrees(th_1_codo_arriba[:tam]))  # Usar th_1_values en lugar de th_1
plt.plot(t[:tam], np.degrees(th_2_codo_arriba[:tam]))  # Usar th_2_values en lugar de th_2
plt.xlim([-2, 360])
plt.ylim([-90, 90])
plt.xlabel("Tiempo (t)")
plt.ylabel("Grados (°)")
plt.legend(["Theta 1", "Theta 2"])

plt.subplot(1, 2, 2)
plt.title("Graficas de Thetas para codo arriba")
plt.plot(t[:tam], np.degrees(th_1_codo_abajo[:tam]))  # Usar th_1_values en lugar de th_1
plt.plot(t[:tam], np.degrees(th_2_codo_abajo[:tam]))  # Usar th_2_values en lugar de th_2
plt.xlim([-2, 360])
plt.ylim([-90, 90])
plt.xlabel("Tiempo (t)")
plt.ylabel("Grados (°)")
plt.legend(["Theta 1", "Theta 2"])
plt.show()

