import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import os

def clear_console():
    #para windows
        _ = os.system('cls')
np.set_printoptions(precision=3)
clear_console()

L1 = 200
L2 = 100
delta = 5
t_fin = 360
q_p = np.array([[63.61], [-115.94]])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
ax1.set_aspect('equal')
ax1.set_xlabel('Px')
ax1.set_ylabel('Py')
ax1.set_xlim(0, 260)
ax1.set_ylim(-25, 200)

ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Error')
ax2.set_xlim(0, t_fin)
ax2.set_title('Error en Px y Py')

traj_circle = Circle((200, 100), 50, color='g', linestyle='--', fill=False)
ax1.add_patch(traj_circle)
th1 =   []
th2 =   []
th1v =   []
th2v =   []
Px_e = []
Py_e = []

for t in np.arange(0, t_fin, delta):
    # Jacobiana
    J = np.array([[-(L2 * np.sin(np.radians(q_p[0, 0] + q_p[1, 0]))) - (L1 * np.sin(np.radians(q_p[0, 0]))), -(L2 * np.sin(np.radians(q_p[0, 0] + q_p[1, 0])))],
                  [(L2 * np.cos(np.radians(q_p[0, 0] + q_p[1, 0]))) + (L1 * np.cos(np.radians(q_p[0, 0]))), (L2 * np.cos(np.radians(q_p[0, 0] + q_p[1, 0])))]])
    
    # Velocidad de las articulaciones
    ve = np.array([[50 * np.sin(np.radians(t))], [-50 * np.cos(np.radians(t))]])
    
    # Cálculo del vector Q
    q_prima = np.dot(np.linalg.inv(J), ve)
    
    # Integración de Euler
    q_n = q_p + (q_prima * delta)
    
    # Valor deseado
    Px_d = 200 - 50 * np.cos(np.radians(t))
    Py_d = 100 - 50 * np.sin(np.radians(t))
    
    # Valores con integración de Euler
    Px = L1 * np.cos(np.radians(q_p[0, 0])) + L2 * np.cos(np.radians(q_p[0, 0] + q_p[1, 0]))
    Py = L1 * np.sin(np.radians(q_p[0, 0])) + L2 * np.sin(np.radians(q_p[0, 0] + q_p[1, 0]))
    
    # Dibujar
    line1 = ax1.plot([0, L1 * np.cos(np.radians(q_p[0, 0]))], [0, L1 * np.sin(np.radians(q_p[0, 0]))], 'b-')[0]  # Eslabón 1
    line2 = ax1.plot([L1 * np.cos(np.radians(q_p[0, 0])), Px], [L1 * np.sin(np.radians(q_p[0, 0])), Py], 'b-')[0]  # Eslabón 2
    ax1.plot(Px, Py, 'bo', markersize=1.5)  # Punto final más pequeño
    
    # Error
    Px_e.append(abs(Px_d - Px))
    Py_e.append(abs(Py_d - Py))
    # Actualizar gráficos
    ax2.clear()
    ax2.plot(np.arange(0, t+delta, delta), Px_e[:len(Px_e)], label='Error en Px')
    ax2.plot(np.arange(0, t+delta, delta), Py_e[:len(Py_e)], label='Error en Py')
    ax2.legend()
    
    plt.pause(0.001)
    
    # Eliminar las líneas del robot excepto en la última iteración
    if t != t_fin - delta:
        line1.remove()
        line2.remove()
    
    q_p = q_n
    #Almacenar posicion
    th1.append(q_p[0,0])
    th2.append(q_p[1,0])
    #Almacenar velocidad
    th1v.append(ve[0,0])
    th2v.append(ve[1,0])


fig, (ax3, ax4) = plt.subplots(2, 1, figsize=(8, 6))
#Gráfico para θ1 y θ2
ax3.set_xlabel('Tiempo')
ax3.set_ylabel('Ángulo (grados)')
ax3.set_title('Ángulos de Articulación')
ax3.set_xlim(0, t_fin)

#Gráfico para θ1' y θ2'
ax4.set_xlabel('Tiempo')
ax4.set_ylabel('Velocidad Angular')
ax4.set_title('Velocidades de Articulación')
ax4.set_xlim(0, t_fin)
ax3.plot(np.arange(0, t + delta, delta), th1, label='θ1')
ax3.plot(np.arange(0, t + delta, delta), th2, label='θ2')
ax3.legend()

ax4.plot(np.arange(0, t + delta, delta), th1v, label='θ1\'')
ax4.plot(np.arange(0, t + delta, delta), th2v, label='θ2\'')
ax4.legend()

plt.tight_layout()
plt.show()

