# Robotica_2024_1_Airy
- **Autor:** Mario Airy Hernandez Osorio
- **Institución:** Universidad Autónoma de Querétaro (UAQ)
- **Curso:** Robótica
- **Instructor:** Dr. Gerardo Pérez Soto
- **Año:** 2024-1

Descripción del Repositorio de Códigos de Python para Cálculo de Cinemática de Robots de N GDL
Este repositorio contiene tres programas en Python diseñados para calcular la Matriz de Transformación Homogénea (MTH), la matriz Jacobiana, y los vectores de velocidad de un robot con N Grados de Libertad (GDL). A continuación, se presenta una descripción detallada de cada uno de los programas incluidos:
## 1er parcial: 

### Cálculo de la MTH de un Robot de N GDL
Nombre del codigo "Parametros_DH"
#### Funcionalidad

Este programa permite al usuario ingresar los parámetros de Denavit-Hartenberg (DH) para cada articulación de un robot de N GDL y calcular la Matriz de Transformación Homogénea (MTH) final. Adicionalmente, calcula los ángulos de Euler y el vector de posición del actuador final.

#### Características

- Entrada interactiva de los parámetros DH.
- Conversión de ángulos de grados a radianes.
- Cálculo y visualización de las matrices de transformación individuales para cada articulación.
- Multiplicación de las matrices de transformación para obtener la MTH final.
- Cálculo de los ángulos de Euler y el vector de posición.

#### Ejecución

Para ejecutar el programa, basta con correr el script en un entorno de Python y seguir las instrucciones que aparecen en la consola para ingresar los datos requeridos.

### Cálculo de la MTH de un Robot de N GDL Simbólico
Nombre del código: "Parametros_DH_syms"

#### Funcionalidad
Este programa permite al usuario calcular la Matriz de Transformación Homogénea (MTH) para un robot de N grados de libertad (GDL) utilizando parámetros de Denavit-Hartenberg (DH) simbólicos. Adicionalmente, el programa calcula el vector de posición y la matriz de rotación del actuador final.

#### Características
- Entrada interactiva de parámetros DH: Los usuarios pueden ingresar los parámetros de cada articulación del robot.
- Conversión de ángulos: Convierte los ángulos de grados a radianes según sea necesario.
- Cálculo de matrices de transformación: Calcula y visualiza las matrices de transformación individuales para cada articulación.
- Multiplicación de matrices: Multiplica las matrices de transformación para obtener la MTH final.
- Cálculo del vector de posición y matriz de rotación: Extrae y muestra el vector de posición y la matriz de rotación del actuador final.
#### Ejecución
Para ejecutar el programa, basta con correr el script en un entorno de Python y seguir las instrucciones que aparecen en la consola para ingresar los datos requeridos.

### Solucionar Sistemas de Ecuaciones con Métodos Numéricos 
Nombre del código: "Newton_Raphson"

#### Funcionalidad
Este programa resuelve un sistema de ecuaciones no lineales utilizando el método fsolve de SciPy. Las ecuaciones están definidas con respecto a un sistema físico que involucra ángulos y una variable de ajuste.

#### Características
- Definición de funciones de ecuaciones: Las funciones equations y jacobian encapsulan las ecuaciones y la matriz jacobiana del sistema respectivamente.
- Ajuste de ángulos: Asegura que los ángulos calculados estén en el rango [0, 360) grados.
- Uso de fsolve de SciPy: Utiliza un método robusto para encontrar la solución numérica a las ecuaciones no lineales.
- Conversión y salida de resultados: Los resultados finales se convierten a grados y se imprimen de manera clara y legible.

#### Ejecución
Modificar los parametros dentro del codigo para el sistema de ecuaciones que deseas resolver
---

## Programa 2: Cálculo de la MTH, Jacobiana y Velocidad de un Robot de N GDL

### Funcionalidad

Este programa calcula las matrices de transformación homogénea, la matriz Jacobiana y el vector de velocidad de un robot de N GDL. El usuario ingresa los parámetros de DH y define el tipo de cada articulación (revoluta o prismática).

### Características

- Definición de funciones trigonométricas con grados.
- Cálculo y visualización de las matrices de transformación homogénea para cada articulación.
- Multiplicación de las matrices para obtener la MTH global.
- Construcción de la matriz Jacobiana.
- Cálculo del vector de velocidad para el actuador final.

### Ejecución

El programa se ejecuta en un entorno de Python, solicitando al usuario que ingrese los parámetros DH y el tipo de cada articulación. Luego, muestra los resultados de las matrices y los cálculos de velocidad.

---

## Programa 3: Cálculo de la MTH, Jacobiana y Velocidad con Simulación de Movimiento

### Funcionalidad

Este programa extiende las funcionalidades del segundo programa al incluir una simulación del movimiento del robot. Permite calcular la MTH, la matriz Jacobiana, el vector de velocidad y realizar una simulación de la trayectoria del robot.

### Características

- Cálculo de las matrices de transformación homogénea.
- Construcción de la matriz Jacobiana.
- Cálculo del vector de velocidad del actuador final.
- Simulación de movimiento utilizando la integración de Euler.
- Visualización gráfica de la trayectoria del robot y del error en la posición.

### Ejecución

El programa se ejecuta en un entorno de Python con soporte para gráficos (usando matplotlib). Permite al usuario ingresar los parámetros necesarios y visualizar la trayectoria simulada del robot junto con el error de posición en gráficos.
