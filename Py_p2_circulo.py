##Programa para obtener la posicion utilizando intergacion de euler para un robot de 2GDL RIIR
##Creado por:Mario Airy Hernandez Osorio
##UAQ2023-1, Robotica, Dr.Gerardo Perez Soto
##################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------


#----------------------------------Lazo abierto sin perfil de velocidad----------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import os

def clear_console():
    # Para Windows
    _ = os.system('cls')

np.set_printoptions(precision=3)
clear_console()


L1 = 104        # Valor del eslabón 1
L2 = 181.36     # Valor del eslabón 2
delta = 5
t_fin = 360
q_p = np.array([[104], [-71]])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
ax1.set_aspect('equal')
ax1.set_xlabel('Px')
ax1.set_ylabel('Py')
ax1.set_xlim(-70, 200)
ax1.set_ylim(-10, 250)

ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Error')
ax2.set_xlim(0, t_fin)
ax2.set_title('Error en Px y Py')

traj_circle = Circle((155, 200), 25, color='g', linestyle='--', fill=False)
ax1.add_patch(traj_circle)
th1 = []
th2 = []
th1v = []
th2v = []
#Vector para velocidad del actuador final
Ve_act  = []
Ve_actx = []
Ve_acty = []
#Vectores para el EMC
Px_e = []
Py_e = []


for t in np.arange(0, t_fin, delta):
    # Jacobiana
    J = np.array([[-(L2 * np.sin(np.radians(q_p[0, 0] + q_p[1, 0]))) - (L1 * np.sin(np.radians(q_p[0, 0]))), -(L2 * np.sin(np.radians(q_p[0, 0] + q_p[1, 0])))],
                  [(L2 * np.cos(np.radians(q_p[0, 0] + q_p[1, 0]))) + (L1 * np.cos(np.radians(q_p[0, 0]))), (L2 * np.cos(np.radians(q_p[0, 0] + q_p[1, 0])))]])
    
    # Velocidad de las articulaciones
    ve = np.array([[25 * np.sin(np.radians(t))], [-25 * np.cos(np.radians(t))]])
    Veact = np.sqrt(np.square(ve[0, 0]) + np.square(ve[1, 0]))  # Magnitud de la velocidad
    # Cálculo del vector Q
    q_prima = np.dot(np.linalg.inv(J), ve)
    
    # Integración de Euler
    q_n = q_p + (q_prima * delta)
    
    # Valor deseado
    Px_d = 155 - 25 * np.cos(np.radians(t))
    Py_d = 200 - 25 * np.sin(np.radians(t))
    
    # Valores con integración de Euler
    Px = L1 * np.cos(np.radians(q_p[0, 0])) + L2 * np.cos(np.radians(q_p[0, 0] + q_p[1, 0]))
    Py = L1 * np.sin(np.radians(q_p[0, 0])) + L2 * np.sin(np.radians(q_p[0, 0] + q_p[1, 0]))
    
    # Dibujar
    line1 = ax1.plot([0, L1 * np.cos(np.radians(q_p[0, 0]))], [0, L1 * np.sin(np.radians(q_p[0, 0]))], 'b-')[0]  # Eslabón 1
    line2 = ax1.plot([L1 * np.cos(np.radians(q_p[0, 0])), Px], [L1 * np.sin(np.radians(q_p[0, 0])), Py], 'b-')[0]  # Eslabón 2
    ax1.plot(Px, Py, 'bo', markersize=0.8)  # Punto final más pequeño
    
    # Error
    Px_e.append(abs(Px_d - Px))
    Py_e.append(abs(Py_d - Py))
    # Actualizar gráficos
    ax2.clear()
    ax2.plot(np.arange(0, t+delta, delta), Px_e[:len(Px_e)], label='Error en Px')
    ax2.plot(np.arange(0, t+delta, delta), Py_e[:len(Py_e)], label='Error en Py')
    ax2.legend()
    
    plt.pause(0.005)
    
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
    #Almacenar velocidad del actuador final
    Ve_actx.append(ve[0,0])
    Ve_acty.append(ve[1,0])
    Ve_act.append(Veact)

# Para almacenarlo en un archivo txt puedes usar:
np.savetxt('th1_euler_abierto.txt',  th1, fmt='%2f')
np.savetxt('th2_euler_abierto.txt',  th2, fmt='%2f')

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


# Convert to numpy arrays for easier handling (especially if you're using lists)
Ve_actx = np.array(Ve_actx)
Ve_acty = np.array(Ve_acty)
tiempo = np.arange(0, len(Ve_actx) * delta, delta)  # Recalculate time to match the lengths

# Plotting the velocity components
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title('Componentes de la Velocidad del Actuador')
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Velocidad (cm/s)')
ax.plot(tiempo, Ve_actx, label='Componente X', color='red')
ax.plot(tiempo, Ve_acty, label='Componente Y', color='blue')
ax.plot(tiempo, Ve_act, label='Magnitud del perfil', color='green')
ax.legend()

plt.tight_layout()
plt.show()



#-----------------------------------------------------------------------------------------------------------------

#---------------------------------Con Perfil de Velocidad-------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------


#Primer codigo con perfil
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.patches import Circle
# import os

# def clear_console():
#     # Para Windows
#     _ = os.system('cls')

# def perfil_trapezoidal(t, t_total, v_max,offset):
#     acel_time = t_total * 0.10  # Acelera durante el 25% del tiempo total
#     decel_time = t_total * 0.9 # Comienza a desacelerar al 75% del tiempo total

#     if t < acel_time:
#         return (v_max / acel_time) * t + offset
#     elif t < decel_time:
#         return v_max + offset
#     else:
#         return v_max - (v_max / (t_total - decel_time)) * (t - decel_time) + offset

# np.set_printoptions(precision=3)
# clear_console()

# L1 = 104        # Valor del eslabón 1
# L2 = 181.36     # Valor del eslabón 2
# delta = 5
# t_fin = 360
# q_p = np.array([[110], [-80]])


# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
# ax1.set_aspect('equal')
# ax1.set_xlabel('Px')
# ax1.set_ylabel('Py')
# ax1.set_xlim(-70, 200)
# ax1.set_ylim(-10, 250)

# ax2.set_xlabel('Tiempo')
# ax2.set_ylabel('Error')
# ax2.set_xlim(0, t_fin)
# ax2.set_title('Error en Px y Py')

# traj_circle = Circle((150, 190), 25, color='g', linestyle='--', fill=False)
# ax1.add_patch(traj_circle)
# th1 = []
# th2 = []
# th1v = []
# th2v = []
# #Vector para velocidad del actuador final
# Ve_act  = []
# Ve_actx = []
# Ve_acty = []
# #Vectores para el EMC
# Px_e = []
# Py_e = []

# for t in np.arange(0, t_fin , delta):
#     # Aplicando perfil trapezoidal para las velocidades
#     ve = np.array([[ perfil_trapezoidal(t, t_fin, 20 , 5) * np.sin(np.radians(t))], 
#                    [-perfil_trapezoidal(t, t_fin, 20 , 5) * np.cos(np.radians(t))]])
#     Veact = np.sqrt(np.square(ve[0, 0]) + np.square(ve[1, 0]))  # Magnitud de la velocidad
#     # Jacobiana
#     J = np.array([[-(L2 * np.sin(np.radians(q_p[0, 0] + q_p[1, 0]))) - (L1 * np.sin(np.radians(q_p[0, 0]))), -(L2 * np.sin(np.radians(q_p[0, 0] + q_p[1, 0])))],
#                   [(L2 * np.cos(np.radians(q_p[0, 0] + q_p[1, 0]))) + (L1 * np.cos(np.radians(q_p[0, 0]))), (L2 * np.cos(np.radians(q_p[0, 0] + q_p[1, 0])))]])
    
#     # Cálculo del vector Q
#     q_prima = np.dot(np.linalg.inv(J), ve)
    
#     # Integración de Euler
#     q_n = q_p + (q_prima * delta)
    
#     # Valor deseado
#     Px_d = 150 - 25 * np.cos(np.radians(t))
#     Py_d = 190 - 25 * np.sin(np.radians(t))
    
#     # Valores con integración de Euler
#     Px = L1 * np.cos(np.radians(q_p[0, 0])) + L2 * np.cos(np.radians(q_p[0, 0] + q_p[1, 0]))
#     Py = L1 * np.sin(np.radians(q_p[0, 0])) + L2 * np.sin(np.radians(q_p[0, 0] + q_p[1, 0]))
    
#     # Dibujar
#     line1 = ax1.plot([0, L1 * np.cos(np.radians(q_p[0, 0]))], [0, L1 * np.sin(np.radians(q_p[0, 0]))], 'b-')[0]  # Eslabón 1
#     line2 = ax1.plot([L1 * np.cos(np.radians(q_p[0, 0])), Px], [L1 * np.sin(np.radians(q_p[0, 0])), Py], 'b-')[0]  # Eslabón 2
#     ax1.plot(Px, Py, 'bo', markersize=0.8)  # Punto final más pequeño
    
#     # Error
#     Px_e.append(abs(Px_d - Px))
#     Py_e.append(abs(Py_d - Py))
#     # Actualizar gráficos
#     ax2.clear()
#     ax2.plot(np.arange(0, t+delta, delta), Px_e[:len(Px_e)], label='Error en Px')
#     ax2.plot(np.arange(0, t+delta, delta), Py_e[:len(Py_e)], label='Error en Py')
#     ax2.legend()
    
#     plt.pause(0.001)
    
#     # Eliminar las líneas del robot excepto en la última iteración
#     if t != t_fin - delta:
#         line1.remove()
#         line2.remove()
    
#     q_p = q_n
#     #Almacenar posición
#     th1.append(q_p[0,0])
#     th2.append(q_p[1,0])
#     #Almacenar velocidad
#     th1v.append(q_prima[0,0])
#     th2v.append(q_prima[1,0])
#     #Almacenar velocidad del actuador final
#     Ve_actx.append(ve[0,0])
#     Ve_acty.append(ve[1,0])
#     Ve_act.append(Veact)



# # Para almacenarlo en un archivo txt puedes usar:
# np.savetxt('th1_euler_abierto_perfil.txt', th1, fmt='%2f')
# np.savetxt('th2_euler_abierto_perfil.txt', th2, fmt='%2f')

# fig, (ax3, ax4) = plt.subplots(2, 1, figsize=(8, 6))
# #Gráfico para θ1 y θ2
# ax3.set_xlabel('Tiempo')
# ax3.set_ylabel('Ángulo (grados)')
# ax3.set_title('Ángulos de Articulación')
# ax3.set_xlim(0, t_fin)

# #Gráfico para θ1' y θ2'
# ax4.set_xlabel('Tiempo')
# ax4.set_ylabel('Velocidad Angular')
# ax4.set_title('Velocidades de Articulación')
# ax4.set_xlim(0, t_fin)
# ax3.plot(np.arange(0, t + delta, delta), th1, label='θ1')
# ax3.plot(np.arange(0, t + delta, delta), th2, label='θ2')
# ax3.legend()

# ax4.plot(np.arange(0, t + delta, delta), th1v, label='θ1\'')
# ax4.plot(np.arange(0, t + delta, delta), th2v, label='θ2\'')
# ax4.legend()

# # Convert to numpy arrays for easier handling (especially if you're using lists)
# Ve_actx = np.array(Ve_actx)
# Ve_acty = np.array(Ve_acty)
# tiempo = np.arange(0, len(Ve_actx) * delta, delta)  # Recalculate time to match the lengths

# # Plotting the velocity components
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.set_title('Componentes de la Velocidad del Actuador')
# ax.set_xlabel('Tiempo (s)')
# ax.set_ylabel('Velocidad (cm/s)')
# ax.plot(tiempo, Ve_actx, label='Componente X', color='red')
# ax.plot(tiempo, Ve_acty, label='Componente Y', color='blue')
# ax.plot(tiempo, Ve_act, label='Magnitud del perfil', color='green')
# ax.legend()
# plt.tight_layout()
# plt.show()
