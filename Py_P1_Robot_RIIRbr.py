import numpy as np
import matplotlib.pyplot as plt
import os

def clear_console():
    # Para Windows
    _ = os.system('cls')

np.set_printoptions(precision=3)
clear_console()

# Valores conocidos
l1 = 104        # Valor del eslabón 1
l2 = 181.36     # Valor del eslabón 2
Px_values = []
Py_values = []
#Las siguientes contantes son las necesarias para el incremento dentro de cada funcion temporal
delta0 = (220 - 218) / 15
delta1 = (253 - 218) / 30
delta2 = (256 - 253) / 10
delta3 = (256 - 252.5) / 5
delta4 = (255 - 252.5) / 10
delta5 = (255 - 250.5) / 10
delta6 = (259.720477 - 250.5) / 15#
delta7 = (265 - 259.720477) / 5
delta8 = (265 - 258) / 15
delta9 = (263.5 - 258)/15
delta10 = (271 - 263.5)/15
delta11 = (271 - 267) / 15
delta12 = (273 - 267) / 5
delta13 = (279.499088 - 273) / 15
delta14 = (279.499088 - 273) / 10
delta15 = (273 - 272) / 10
delta16 = (272 - 268.5) / 5
delta17 = (268.5 - 267) / 15
r = np.sqrt(143.680010255)
delta18 = (247.9643865176706 - 217) / 30
delta19 = (217 - 214.5) / 10
#-------------------------------------------------------------------------------------------#
#Creacion de la ruta dependiendo de las ecuaciones temporales de nuestra figura
for t in range(-16, 271, 1):
    if 0 < t <= 30:             #Ecuacion 1
        Px = 218 + delta1 * t
        Py = 0.667841982 * Px - 113.37408263
    elif 30 < t <= 40:          #Ecuacion 2
        Px = 253 + delta2 * (t - 30)
        Py = -4.67489387 * Px + 1238.33808907
    elif 40 < t <= 45:          #Ecuacion 3
        Px = 256 - delta3 * (t - 40)
        Py = 0.364277444 * Px - 51.6897686554
    elif 45 < t <= 55:          #Ecuacion 4
        Px = 252.5 + delta4 * (t - 45)
        Py = -4.16490545 * Px + 1091.92891272
    elif 55 < t <= 65:          #Ecuacion 5
        Px = 255 - delta5 * (t - 55)
        Py = 1.6055191084 * Px - 379.529350125
    elif 65 < t <= 80:          #Ecuacion 6
        Px = 250.5 + delta6 * (t - 65)
        Py = -1.34866227 * Px + 360.4930866
    elif 80 < t <= 85:          #Ecuacion 7
        Px = 259.72040779 + delta7 * (t - 80)
        Py = 0.8325815348 * Px - 206.020445379
    elif 85 < t <= 100:         #Ecuacion 8
        Px = 265 - delta8 * (t - 85)
        Py = -1.166349214 * Px + 323.695673287
    elif 100 < t <= 115:        #Ecuacion 9
        Px = 258 + delta9 * (t - 100)
        Py = 1.65978069685 * Px - 405.445327923
    elif 115 < t <= 130:        #Ecuacion 10
        Px = 263.5 + delta10 * (t - 115)
        Py = -0.9905388044 * Px + 292.91386067315
    elif 130 < t <= 145:        #Ecuacion 11
        Px = 271 - delta11 * (t - 130)
        Py = 2.4144383358 * Px - 629.834944358659
    elif 145 < t <= 150:        #Ecuacion 12
        Px = 267 + delta12 * (t - 145)
        Py = -0.3866818867 * Px + 118.06415507786
    elif 150 < t <= 165:        #Ecuacion 13
        Px = 273 + delta13 * (t - 150)
        Py = 2.18266525520 * Px - 583.3676146719
    elif 165 < t <= 175:        #Ecuacion 14
        Px = 279.499088 - delta14 * (t - 165)
        Py = -1.0320461252 * Px + 315.14128609597
    elif 175 < t <= 185:        #Ecuacion 15
        Px = 273 - delta15 * (t - 175)
        Py = -9.9363423822 * Px + 2746.0141642614
    elif 185 < t <= 190:        #Ecuacion 16
        Px = 273 - delta16 * (t - 185)
        Py = -0.1917802769 * Px + 95.493271603267
    elif 190 < t <= 205:        #Ecuacion 17
        Px = 268.5 - delta17 * (t - 190)
        Py = -8.3309860906 * Px + 2280.87003259301
    elif 205 < t <= 230:        #Ecuacion 18
        Px = 259.3717461842596 -  r * np.cos(np.radians(129.523548)+ 8.5 *np.radians(t-205))
        Py = 65.7428133379 -  r * np.sin(np.radians(129.523548)+ 8.5 * np.radians(t-205))
    elif 230 < t <= 260:        #Ecuacion 19
        Px = 247.9643865176706 - delta18 * (t - 230)
        Py = 0.6335445291932 * Px - 87.6723419119741
    elif 260 < t <= 270:        #Ecuacion 20
        Px = 217 - delta19 * (t - 260)
        Py = -5.656312455734 * Px + 1277.2266238172365
    else:                       #Ecuacion 21
        Px = 220 - delta0 * (t + 15)
        Py = -6.107734727669 * Px + 1363.70164008716
    #print(t, " ", Px, " ", Py)         #Imprime los valores para (X,Y) de nuestra ruta deseada
    Px_values.append(Px)        #Guarda los valores de Px
    Py_values.append(Py)        #Guarda los valores de Py

tam = len(Px_values)
th_1_codo_arriba = np.zeros(tam)  # Matriz para almacenar th_1
th_2_codo_arriba = np.zeros(tam)  # Matriz para almacenar th_2
th_1_codo_abajo = np.zeros(tam)  # Matriz para almacenar th_1
th_2_codo_abajo = np.zeros(tam)  # Matriz para almacenar th_2

for j in range(1):  # For de repeticiones
    plt.pause(1)
    for i in range(tam):
        # 1era sustitución
        u = l1 ** 2 + Px_values[i] ** 2 + Py_values[i] ** 2 - l2 ** 2
        v = -2 * l1 * Px_values[i]
        w = -2 * l1 * Py_values[i]

        # 2da sustitución
        a = u - v  # cuadrado
        b = 2 * w  # lineal
        c = u + v  # cte

        # Codo arriba
        th_11 = 2 * np.arctan2((-b + np.sqrt(b ** 2 - 4 * a * c)), (2 * a))
        th_2a = np.arctan2((Py_values[i] - l1 * np.sin(th_11)), (Px_values[i] - l1 * np.cos(th_11)))
        th_12 = th_2a - th_11
        x11 = l1 * np.cos(th_11)
        y11 = l1 * np.sin(th_11)
        x12 = l1 * np.cos(th_11) + l2 * np.cos(th_11 + th_12)
        y12 = l1 * np.sin(th_11) + l2 * np.sin(th_11 + th_12)

        th_1_codo_arriba[i] = th_11  # Almacena el valor de th_1
        th_2_codo_arriba[i] = th_12  # Almacena el valor de th_2

        # Codo abajo
        th_21 = 2 * np.arctan2((-b - np.sqrt(b ** 2 - 4 * a * c)), (2 * a))
        th_2b = np.arctan2((Py_values[i] - l1 * np.sin(th_21)), (Px_values[i] - l1 * np.cos(th_21)))
        th_22 = th_2b - th_21
        x21 = l1 * np.cos(th_21)
        y21 = l1 * np.sin(th_21)
        x22 = l1 * np.cos(th_21) + l2 * np.cos(th_21 + th_22)
        y22 = l1 * np.sin(th_21) + l2 * np.sin(th_21 + th_22)

        th_1_codo_abajo[i] = th_21  # Almacena el valor de th_1
        th_2_codo_abajo[i] = th_22  # Almacena el valor de th_2

        plt.figure(1)
        plt.clf()  # Limpiar la figura

        # Gráfico codo arriba
        plt.subplot(1, 2, 1)
        plt.title("Codo arriba")
        plt.plot(Px_values, Py_values)
        plt.plot([0, x11], [0, y11], 'rd-')
        plt.plot([x11, x12], [y11, y12], 'bd-')
        plt.xlim([-10, 300])
        plt.ylim([-50, 100])
        plt.legend(["Curva de movimiento", "l1", "l2"])

        #Gráfico codo abajo
        plt.subplot(1, 2, 2)
        plt.title("Codo abajo")
        plt.plot(Px_values, Py_values)
        plt.plot([0, x21], [0, y21], 'rd-')
        plt.plot([x21, x22], [y21, y22], 'bd-')
        plt.xlim([-10, 300])
        plt.ylim([-100, 100])
        plt.legend(["Curva de movimiento", "l1", "l2"])

        plt.show(block=False)
        plt.pause(0.01)

# Para almacenarlo en un archivo txt puedes usar:
np.savetxt('th1_br.txt',  np.degrees(th_1_codo_abajo), fmt='%f')
np.savetxt('th2_br.txt',  np.degrees(th_2_codo_abajo), fmt='%f')

plt.figure(2)
plt.subplot(1, 2, 1)
plt.title("Gráficas de Thetas para codo arriba")
plt.plot(range(tam), np.degrees(th_1_codo_arriba))  # Usar th_1_values en lugar de th_1
plt.plot(range(tam), np.degrees(th_2_codo_arriba))  # Usar th_2_values en lugar de th_2
plt.xlim([-18, 300])
plt.ylim([-90, 90])
plt.xlabel("Tiempo (t)")
plt.ylabel("Grados (°)")
plt.legend(["Theta 1", "Theta 2"])

plt.subplot(1, 2, 2)
plt.title("Graficas de Thetas para codo Abajo")
plt.plot(range(tam), np.degrees(th_1_codo_abajo))  # Usar th_1_values en lugar de th_1
plt.plot(range(tam), np.degrees(th_2_codo_abajo))  # Usar th_2_values en lugar de th_2
plt.xlim([-18, 300])
plt.ylim([-90, 90])
plt.xlabel("Tiempo (t)")
plt.ylabel("Grados (°)")
plt.legend(["Theta 1", "Theta 2"])
plt.show()
