##Programa para obtener la MTH por art,MTH final,Jacobina y vector velocidad de un robot de n GDL
##Creado por:Mario Airy Hernandez Osorio
##UAQ2023-1, Robotica, Dr.Gerardo Perez Soto
import numpy as np
import os
from sympy import symbols, cos, sin, Matrix, simplify, pi
def clear_console():
    #para windows
        _ = os.system('cls')
np.set_printoptions(precision=3)
clear_console()
syms = symbols('Vx th1_p th2_p th3_p P4_p th5_p th6_p')
# Definición de funciones trigonométricas con grados
def sind(deg):
    return np.sin(np.deg2rad(deg))

def cosd(deg):
    return np.cos(np.deg2rad(deg))

# Definición de parámetros de articulaciones (t, d, a, alfa) para cada articulación
DH = [
    #Robot problema 4
    #  {"t": 25, "d": 0, "a": 20, "alfa": 0},
    #  {"t": 0, "d": 0, "a": 10, "alfa": 0},
     #robot esferico
    {"t": -60, "d": 65, "a": 0, "alfa": -90},
    {"t": 90, "d": 0, "a": 0, "alfa": 90},
    {"t": 30, "d": 83, "a": 0, "alfa": 0},

    #Robot 2gdl
    #  {"t": -30, "d": 0, "a": 0, "alfa": 90},
    #  {"t": 90, "d": 3, "a": 4, "alfa": 0}
]

##ingresa 0= rev,1=pris

#Robot esferico
art=[0,0,0]
#Robot 2gdl
#art = [0,0]
i=1
#Vector velocidad actuador final debe ser de 6x1
vel = np.array([
            #Robot esferico
            [63.75],
            [73.6122],
            [-110.4148],
            [1.7321],
            [1.5],
            [2]
            #Robot problema 4
            # [3],
            # [-2],
            # [0],
            # [0],
            # [0],
            # [0],
            #Robot 2gdl problema 1
            # [-4.33],
            # [ 2.5 ],
            # [ 0.  ],
            # [-2.5 ],
            # [-4.33],
            # [ 5.  ]
             ])
# Inicialización de matrices
A_matrices = []
Z=[]
Pos=[]
Vart=[]
Jacobianas = []
# Construcción de la MTH
for param in DH:
    A_i = np.array([
        [cosd(param["t"]), -sind(param["t"]) * cosd(param["alfa"]), sind(param["t"]) * sind(param["alfa"]), param["a"] * cosd(param["t"])],
        [sind(param["t"]), cosd(param["t"]) * cosd(param["alfa"]), -cosd(param["t"]) * sind(param["alfa"]), param["a"] * sind(param["t"])],
        [0, sind(param["alfa"]), cosd(param["alfa"]), param["d"]],
        [0, 0, 0, 1]
    ])
    np.set_printoptions(suppress=True)
    A_matrices.append(A_i)

print("Bienvenido\nEl programa obtendra los siguientes datos:\n1.Parametros de DH \n2.MTH por articulacion\n3.Multiplicacion de las Matrices MTH0_i \n4.Articulaciones del Robot\n5.Matriz Jacobiana (Jn)\n6.Vector velocidad (Qn)")
print("\n-----------------------------------------------------------------------")
print("1.Parametros de DH")
# Imprimir la cabecera
print(f"{'art':<5} | {'thi':<5} | {'d i':<5} | {'ai':<5} | {'alfai':<5} |")
print("-" * 40)

# Imprimir los valores de cada diccionario
for item in DH:
    print(f"{i:<5} |{item['t']:<5} | {item['d']:<5} | {item['a']:<5} | {item['alfa']:<5} |")
    i+=1
print("\n-----------------------------------------------------------------------")

print("\n2.MTH por articulacion\n")
i=0
#matrices de tranformacion homogenia una a una
for A_i in A_matrices:
    print(f"MTH_{i+1}:\n{A_i}")
    i+=1
print("\n-----------------------------------------------------------------------")

# Matrices MTH0_i
print("\n3.Matrices MTH0_i\n")
MTH0_i = np.eye(4)
for i, A_i in enumerate(A_matrices):
    MTH0_i = np.dot(MTH0_i, A_i)
    Z.append(MTH0_i[:3, 2])  # Calcula Z0_i basado en la matriz A_i actual
    Pos.append(MTH0_i[:3, 3])  # Calcula pos_i basado en la matriz A_i actual
    print(f"MTH_0_{i+1}:\n{MTH0_i}")

print("\n-----------------------------------------------------------------------")
print("\n4.El orden de las articulaciones es:")
cont=1
for i in art:
    if i==0:
        print("Art",cont," Revoluta",sep="")
    else:
        print("Art",cont," Prismatico",sep="")
    cont+=1
print("\n-----------------------------------------------------------------------")
# Construcción de las matrices Jacobianas Jn
print("\n5.Matriz Jacobiana Jn\n")
Z0_0 = np.array([0, 0, 1])  # Vector z0_0
ceros = np.array([0, 0, 0])  # vector ceros
P_f = MTH0_i[:3, 3]


for i, A_i in enumerate(A_matrices):
    if i == 0:  # Primera articulación
        if art[i]==0:                                   #art es una revoluta
            J = np.hstack((np.cross(Z0_0, P_f), Z0_0))
        else:                                   #art es un prismatico
            J = np.hstack((Z0_0, ceros))
        
        Jacobianas.append(J)  

    else:
        if art[i]==0:
            J = np.hstack((np.cross(Z[i-1], (P_f-Pos[i-1])), Z[i-1]))
        else:
            J = np.hstack((Z[i-1], ceros))

        Jacobianas.append(J)
Jn_matrix = np.vstack(Jacobianas).T
print("Jn:\n",Jn_matrix)
print("\n-----------------------------------------------------------------------")

print("\n5.inversa Jn\n")

n, m = Jn_matrix.shape  # n = filas, m = columnas
if n == m:
    if np.linalg.det(Jn_matrix) == 0:
        print('La matriz Jacobiana es singular')
    else:
        q_p = np.linalg.inv(Jn_matrix) @ vel
        print("Vector velocidad de las articulaciones (q_p):\n", q_p)
elif n > m:  # Pseudo-inversa por la izquierda
    Jt_i = np.linalg.inv(Jn_matrix.T @ Jn_matrix) @ Jn_matrix.T
    q_p = Jt_i @ vel
    print("Vector velocidad de las articulaciones (q_p):\n", q_p)
elif n < m:  # Pseudo-inversa por la derecha
    Jt_d = Jn_matrix.T @ np.linalg.inv(Jn_matrix @ Jn_matrix.T)
    q_p = Jt_d @ vel
    print("Vector velocidad de las articulaciones (q_p):\n", q_p)

print("\nPara los valores del actuador final:\nvel:\n",vel)