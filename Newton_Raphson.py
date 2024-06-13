import numpy as np
from scipy.optimize import fsolve

# Define las funciones del sistema de ecuaciones
def equations(vars):
    p3, th1, th2 = vars
    p3 = abs(p3)  # Asegurando que p3 sea no negativo
    eq1 = p3 * np.cos(th1) * np.sin(th2) - 200 * np.sin(th1)
    eq2 = p3 * np.sin(th1) * np.sin(th2) + 200 * np.cos(th1) - 200
    eq3 = p3 * np.cos(th2) - 500
    return [eq1, eq2, eq3]

# Derivadas parciales de las funciones respecto a las variables
def jacobian(vars):
    p3, th1, th2 = vars
    p3 = abs(p3)  # Asegurando que p3 sea no negativo
    dp3 = np.cos(th1) * np.sin(th2)
    dth1 = -p3 * np.sin(th1) * np.sin(th2) - 200 * np.cos(th1)
    dth2 = p3 * np.cos(th1) * np.cos(th2)
    dvars = [[dp3, dth1, dth2],
             [np.sin(th1) * np.sin(th2), p3 * np.cos(th1) * np.sin(th2) - 200 * np.sin(th1), p3 * np.sin(th1) * np.cos(th2)],
             [np.cos(th2), 0, -p3 * np.sin(th2)]]
    return np.array(dvars)

# Ajustar el ángulo para que esté en el rango [0, 360)
def ajustar_angulo(angulo):
    return angulo % 360

# Adivinar una solución inicial
guess = [1, 0.5, 0.5]  # p3, th1, th2

# Usar fsolve para encontrar la solución
solution = fsolve(equations, guess, fprime=jacobian)

# Convertir los ángulos de radianes a grados y ajustarlos al rango [0, 360)
solution_deg = np.degrees(solution[1:])  # th1 y th2
solution_deg = [ajustar_angulo(angle) for angle in solution_deg]

print("Solución encontrada:")
print("p3 =", abs(solution[0]))
print("th1 =", solution_deg[0], "grados")
print("th2 =", solution_deg[1], "grados")
