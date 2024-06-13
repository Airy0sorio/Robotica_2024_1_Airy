# Robotica_2024_1_Airy
- **Autor:** Mario Airy Hernandez Osorio
- **Institución:** Universidad Autónoma de Querétaro (UAQ)
- **Curso:** Robótica
- **Instructor:** Dr. Gerardo Pérez Soto
- **Año:** 2024-1

Descripción del Repositorio de Códigos de Python para Cálculo de Cinemática de Robots de N GDL
Este repositorio contiene tres programas en Python diseñados para calcular la Matriz de Transformación Homogénea (MTH), la matriz Jacobiana, y los vectores de velocidad de un robot con N Grados de Libertad (GDL). A continuación, se presenta una descripción detallada de cada uno de los programas incluidos:
## 1er parcial: 

### 1.1. Cálculo de la MTH de un Robot de N GDL
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

### 1.2. Cálculo de la MTH de un Robot de N GDL Simbólico
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

### 1.3. Solucionar Sistemas de Ecuaciones con Métodos Numéricos 
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

## 2do Parcial: 

### 2.1. Programa para obtener la MTH por art, MTH final, Jacobiana y vector velocidad de un robot de n GDL
Nombre del código: "Jacobiana_directa"

### Funcionalidad

Este programa calcula la Matriz de Transformación Homogénea (MTH) por cada articulación de un robot de N grados de libertad (GDL) utilizando los parámetros de Denavit-Hartenberg (DH). Además, determina la MTH final del robot, la matriz Jacobiana (Jn) y el vector de velocidad del actuador final.

### Características

- Uso de parámetros DH: Permite definir los parámetros de cada articulación (t, d, a, alfa).
- Cálculo de MTH por articulación: Calcula y muestra las matrices de transformación homogénea individuales.
- Multiplicación de matrices: Calcula la MTH final combinando las matrices de transformación de cada articulación.
- Determinación del tipo de articulación: Identifica si cada articulación es revoluta o prismática.
- Construcción de la matriz Jacobiana: Crea la matriz Jacobiana (Jn) para el robot en función de las posiciones articulares y velocidades.
 -Cálculo del vector de velocidad: Utiliza la Jacobiana para determinar el vector de velocidad del actuador final en términos lineales y angulares.

### Ejecución

El programa se ejecuta en un entorno de Python, solicitando al usuario que ingrese los parámetros DH, el tipo de cada articulación y el vector velocidad actuador final debe ser de 6x1. Luego, muestra los resultados de las matrices y los cálculos de velocidad.



### 2.2. Programa para calcular la Jacobiana Inversa de un robot de n GDL
Nombre del código: "Jacobiana_Inversa"

### Funcionalidad

Este programa calcula la matriz Jacobiana inversa de un robot de N grados de libertad (GDL) utilizando los parámetros de Denavit-Hartenberg (DH) especificados. Además, calcula el vector de velocidad de las articulaciones (q_p) a partir del vector de velocidad del actuador final dado.

### Características

- Definición de parámetros DH: Permite ingresar los parámetros de cada articulación (t, d, a, alfa).
- Construcción de la Matriz de Transformación Homogénea (MTH): Calcula las MTH individuales y la MTH final del robot.
- Identificación del tipo de articulación: Determina si cada articulación es revoluta o prismática.
- Construcción de la matriz Jacobiana: Genera la matriz Jacobiana (Jn) para el robot.
- Cálculo de la Jacobiana inversa: Utiliza la pseudo-inversa de la Jacobiana para calcular el vector de velocidad de las articulaciones (q_p) a partir del vector de velocidad del actuador final.

### Ejecución

El programa se ejecuta en un entorno de Python, solicitando al usuario que ingrese los parámetros DH y el tipo de cada articulación. Luego, muestra los resultados de las matrices y los cálculos de velocidad.

### 2.3. Programa para Simulación de Robot de 2 GDL con Integración de Euler
Nombre del código: "Integracion_euler"

### Funcionalidad

Este programa simula el movimiento de un robot de dos grados de libertad (GDL) utilizando integración de Euler para calcular las posiciones articulares y las velocidades. También muestra gráficamente los errores en las coordenadas deseadas y los ángulos de articulación.

### Características

-Longitudes de los brazos: Define las longitudes de los dos brazos del robot.
- Delta de tiempo y tiempo final: Especifica el paso de integración y el tiempo total de simulación.
- Integración de Euler: Utiliza el método de Euler para calcular las posiciones articulares y las velocidades angulares a partir de las velocidades lineales deseadas.
- Visualización Gráfica: Muestra gráficos en tiempo real de las posiciones del robot, errores en las coordenadas deseadas y ángulos de articulación.

### Ejecución

- Interacción con el programa:
Observa la simulación en tiempo real del movimiento del robot y los gráficos que muestran los errores en las coordenadas deseadas y los ángulos de articulación.
- Visualización de resultados:
Después de la ejecución, el programa muestra dos gráficos adicionales con los ángulos de articulación y sus velocidades angulares a lo largo del tiempo.

---

## Proyectos
### 1er Parcial
Nombre de los codigos: "Py_P1_Robot_RIIRXX" y "Py_P1_xxx"

#### Descripción
Los codigos con el incio Py_P1_Robot_RIIR pertenecen al mismo proyecto estos describen el comportamiento de un Robot RIIR de 2 GDL el cual tiene como funcion dibujar diferentes figuras, mientras que "Py_P1_xxx" generan una comunicacion serial con un microcontrolador.

### 2do Parcial

Nombre de los codigos: "Py_P2_Circulo" y "Py_P1_xxx"

#### Descripción
Este programa simula el movimiento de un robot de 2 GDL utilizando el método de integración de Euler. Calcula las posiciones articulares, la velocidad del actuador final y muestra gráficamente los errores en las coordenadas deseadas y las características de movimiento.

####  Cálculos Principales:

- Calcula la Jacobiana del robot en cada iteración.
- Determina la velocidad de las articulaciones y el vector Q utilizando la Jacobiana y las velocidades deseadas.
- Integra utilizando el método de Euler para actualizar las posiciones articulares.
- Calcula los valores deseados y con la integración de Euler para comparar y visualizar los errores.

#### Actualización y Visualización Gráfica:

- Dibuja el movimiento del robot y actualiza los gráficos en tiempo real de los errores en las coordenadas deseadas.
- Muestra gráficos adicionales de los ángulos de articulación y sus velocidades angulares a lo largo del tiempo.

#### Almacenamiento de Resultados:

- Guarda los ángulos de articulación (th1_euler_abierto.txt y th2_euler_abierto.txt) en archivos de texto para su posterior análisis.

---

## Instrucciones para ejecutar los archivos en Python

Este repositorio contiene archivos Python para ejecutar diversas funciones. Para hacerlo de manera efectiva, se recomienda utilizar el editor de código Visual Studio Code (VSCode).

### Requisitos previos
Antes de ejecutar los programas, sigue estos pasos:

1. **Instalación de Python:**
   Asegúrate de tener Python instalado, se recomienda la versión 3.11.8.

2. **Creación de una carpeta de proyecto:**
   Crea una carpeta donde se guardarán los archivos y recursos del proyecto.

3. **Creación de un entorno virtual:**
   Abre la terminal integrada de VSCode y ejecuta el siguiente comando para crear un entorno virtual:
   ```
   python -m venv ./env
   ```

4. **Activación del entorno virtual:**
Activa el entorno virtual con el siguiente comando:
    ```
    .env\Scripts\activate
    ```

5. **Instalación de las librerías:**
Instala las librerías utilizadas en el proyecto ejecutando el siguiente comando:
    ```
     pip install -r requirements.txt
    ```

6.**Ejecución del programa**
Una vez configurado el entorno, puedes ejecutar el programa escribiendo el siguiente comando en la terminal:    
    
    ```
    python Nombre_del_archivo.py
    ```
    
Para futuras ejecuciones, simplemente activa el entorno virtual y ejecuta el archivo Python que deseas correr. 
Los pasos 4 y 6 son suficientes para ejecutar cualquier código adicional.
