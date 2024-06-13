import numpy as np
import matplotlib.pyplot as plt
import os

def clear_console():
    # Para Windows
    _ = os.system('cls')

np.set_printoptions(precision=3)
clear_console()

# Valores conocidos
l1 = 104  # Valor del eslabón 1
#l2 = 146  # Valor del eslabón 2
l2 = 181.36
Px_values = []
Py_values = []
delta1=(275 - 215)/90
delta2=(275 - 265)/90
delta3=(265 - 215)/90

for t in range(1, 271, 1):
    if t <= 90:##AB
        Px = 215 + delta1 * t
        Py = 1/6 * Px - 35.833333333
    elif 90 < t <= 180:##AC
        Px = 275 - delta2 * (t - 90)
        Py = 3 * Px - 815
    else:##BC
        Px = 265 - delta3 * (t - 180)
        Py = -0.4 * Px + 86
    #print(t, " ", Px, " ", Py)
    Px_values.append(Px)
    Py_values.append(Py)

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
        plt.xlim([-10, 290])
        plt.ylim([-50, 100])
        plt.legend(["Curva de movimiento", "l1", "l2"])

        # Gráfico codo abajo
        plt.subplot(1, 2, 2)
        plt.title("Codo abajo")
        plt.plot(Px_values, Py_values)
        plt.plot([0, x21], [0, y21], 'rd-')
        plt.plot([x21, x22], [y21, y22], 'bd-')
        plt.xlim([-10, 290])
        plt.ylim([-100, 80])
        plt.legend(["Curva de movimiento", "l1", "l2"])

        plt.show(block=False)
        plt.pause(0.01)

# Para almacenarlo en un archivo txt puedes usar:
np.savetxt('th1_tr.txt',  np.degrees(th_1_codo_abajo), fmt='%f')
np.savetxt('th2_tr.txt',  np.degrees(th_2_codo_abajo), fmt='%f')

plt.figure(2)
plt.subplot(1, 2, 1)
plt.title("Gráficas de Thetas para codo arriba")
plt.plot(range(tam), np.degrees(th_1_codo_arriba))  # Usar th_1_values en lugar de th_1
plt.plot(range(tam), np.degrees(th_2_codo_arriba))  # Usar th_2_values en lugar de th_2
plt.xlim([-2, 190])
plt.ylim([-90, 90])
plt.xlabel("Tiempo (t)")
plt.ylabel("Grados (°)")
plt.legend(["Theta 1", "Theta 2"])

plt.subplot(1, 2, 2)
plt.title("Graficas de Thetas para codo Abajo")
plt.plot(range(tam), np.degrees(th_1_codo_abajo))  # Usar th_1_values en lugar de th_1
plt.plot(range(tam), np.degrees(th_2_codo_abajo))  # Usar th_2_values en lugar de th_2
plt.xlim([-2, 190])
plt.ylim([-90, 90])
plt.xlabel("Tiempo (t)")
plt.ylabel("Grados (°)")
plt.legend(["Theta 1", "Theta 2"])
plt.show()
