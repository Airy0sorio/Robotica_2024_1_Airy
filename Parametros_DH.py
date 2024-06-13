##Programa para obtener la MTH de un robot de n GDL
##Creado por:Mario Airy Hernandez Osorio
##UAQ2024-1, Robotica, Dr.Gerardo Perez Soto
##
##################################################################################################################################

import numpy as np
from scipy.spatial.transform import Rotation
import os

def clear_console():
    #para windows
        _ = os.system('cls')
clear_console()
##configuracion de decimales
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
##################################################################################################################################

#Cuantas articulaciones ingresaras?
print("Bienvenido")
art=int(input("Ingresa el total de articulaciones \n"))
DH=np.zeros(shape=(art,4))
MH=[]
Vector_pos_euler=[]
##################################################################################################################################

#Ciclo para ingresar datos 
for i in range(art):
    print("\nIngresa los valores de la Art ",(i+1))
    th = float(input("Ingresa th_"+str(i+1)+": "))
    d  = float(input("Ingresa d_"+str(i+1)+": "))
    a = float(input("Ingresa a_"+str(i+1)+": "))
    alp  = float(input("Ingresa alfa_"+str(i+1)+": "))
    DH[i]=[th,d,a,alp]
    
print()  
##################################################################################################################################
print("-"*80)
print("\nTabla de Parámetros DH:")
print("| {:^12} | {:^10} | {:^10} | {:^10} | {:^10} |".format("Articulación", "θ (Grad)", "d (ul)", "a (ul)", "α (grad)"))
for i in range(art):
    print("| {:^12} | {:10.4f} | {:10.4f} | {:10.4f} | {:10.4f} |".format(str(i+1), DH[i,0], DH[i,1], DH[i,2], DH[i,3]))

print()
##Cambio de grad to rad
for i in range(art):
    DH[i,0] =(DH[i,0]/180.0)*np.pi
    DH[i,3] =(DH[i,3]/180.0)*np.pi

##################################################################################################################################

#Matriz de transformacion 
for i in range(art):
    MT = [[np.cos(DH[i][0]),-np.sin(DH[i][0])*np.cos(DH[i][3]),np.sin(DH[i][0])*np.sin(DH[i][3]),(DH[i][2])*np.cos(DH[i][0])],
         [np.sin(DH[i][0]),np.cos(DH[i][0])*np.cos(DH[i][3]),-np.cos(DH[i][0])*np.sin(DH[i][3]),(DH[i][2])*np.sin(DH[i][0])],
         [0,np.sin(DH[i][3]),np.cos(DH[i][3]),DH[i][1]],
         [0,0,0,1]]

    MH.append(MT)

##################################################################################################################################
print("-"*80)
##Mostrar matrices homogenias por articulacion
for i in range(len(MH)):
    print("\nMatriz de transformación para articulación", i+1, ":")
    for row in MH[i]:
        print("| {:8.4f} | {:8.4f} | {:8.4f} | {:8.4f} |".format(row[0], row[1], row[2], row[3]))
    print()  # Agrega una línea en blanco entre las matrices

##################################################################################################################################
print("-"*80)
##Multiplicarlas para obtener la MTH
MTH=np.linalg.multi_dot(MH)
print("\nLa matriz de Trandormacion Homogenea de MH0_",art," es:")
for i in MTH:
    print("|","|".join(map("{:8.4f}".format, i)),"|")
##################################################################################################################################
print("\n"+"-"*80)
##angulos de euler
# Extraer la parte de rotación de la matriz de transformación homogénea
R = MTH[:3, :3]
# Crear un objeto de rotación a partir de la matriz de rotación
r = Rotation.from_matrix(R)
print("\nMatriz rotacion:\n",R)
# Obtener los ángulos de Euler
angles = r.as_euler('ZXZ', degrees=True)  # 'ZXZ' representa la secuencia de los ángulos de Euler

# Imprimir los ángulos de Euler
print("\nÁngulos de Euler (grados):","\n[ {:5.4f} ]".format(angles[0]),"\n[ {:5.4f} ]".format(angles[1]),"\n[ {:5.4f} ]".format(angles[2]))
##Vector posicion
Vec_pos = MTH[:3, 3]
print("\nVector posicion:","\n[ {:5.4f} ]".format(Vec_pos[0]),"\n[ {:5.4f} ]".format(Vec_pos[1]),"\n[ {:5.4f} ]".format(Vec_pos[2]))

Vpos_eu=np.concatenate((Vec_pos,angles))
print("\nVector X:(6X1)","\n[ {:5.4f} ]".format(Vpos_eu[0]),"\n[ {:5.4f} ]".format(Vpos_eu[1]),"\n[ {:5.4f} ]".format(Vpos_eu[2]),"\n[ {:5.4f} ]".format(Vpos_eu[3]),"\n[ {:5.4f} ]".format(Vpos_eu[4]),"\n[ {:5.4f} ]".format(Vpos_eu[5]))


##################################################################################################################################
print("-"*35+" Fin del codigo "+"-"*35)
print("-"*35+" Creado por MAHO "+"-"*34)