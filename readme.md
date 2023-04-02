# Primer Seminario de DAA

### Integrantes:
- Raúl Beltrán Gómez C412
- Mauricio Salim Mahmud Sánchez C412

----
## Problema
Dado un array A que contiene solo elementos de 8 tipos distintos, el problema consiste en hallar la subsecuencia máxima T, que cumpla con las restricciones:
-  $\forall C_i,C_j$ conjuntos de elementos de tipos especificos, se tiene que cumplir que $| |C_i| - |C_j| | \le 1 $. 
- los elementos de un mismo conjunto tienen que estar consecutivos en T.

----

## Solución exponencial

Va a consistir en construir todas las posibles subsecuencias de A y verificar que cumplan las restricciones, nos quedamos con la mayor de las cardinalidades de las subsecuencias que sean válidas. Esta solución debido a que es muy intuitiva y facil de demostrar, la usamos para "testear" soluciones mas complejas que proximamente presentamos.

### Correctitud
Dado que estamos construyendo todas las subsecuencias, la subsecuencia con el mayor tamaño y que sea válida la vamos a encontrar en algún punto y vamos guardar su cardinalidad. Una vez encontrada este valor no va a variar ya que encontar una mejor sería la única forma de cambiar el valor pero como esta es la subsecuencia de mayor tamaño, no se va a encontrar una mejor. Luego este algoritmo nos da una solución correcta.

### Complejidad
Esta solución es $T(n)= 2T(n-1) + c$ que usando el teorema maestro llegamos a que $T(n)$ es $O(2^n)$  

    TODO (terminar)


----
## Solución

Definamos las siguientes funciones:

### Función 1:
__input__: int K, cadena S, orden de Clases.

__output__: bool => existe subsecuencia de A donde cada clase tiene exactamente cardinalidad K.


La función recibe el orden en que deben aparecer las clases, sea el orden, sin perder genericidad: [c1,c2,c3,c4,c5,c6,c7,c8], con este dato podemos hacer la siguiente pregunta:

Donde se encuentra el K-esimo elemento de la clase c1?, si existe una posicion que lo contiene nos movemos a esa posicion, es decir desde cero a esa posicion estamos teniendo en cuenta que nos quedaremos solo con los elementos c1. Ahora tenemos un index, una posicion donde nos encontramos que es donde encontramos la K-esima posicion de c1, sea ese indice i. Nuestra siguiente pregunta sera:

Hasta el indice i, cuantas repeticiones de c2 hay? sea la respuesta a ello: x.
Con estos datos nuestra proxima pregunta sera: donde se encuentra el (K+x)-esimo elemento de la clase c2?
Si existe nos movemos al mismo y repetimos el proceso hasta c8. Si todos existen entonces existe una subsecuencia que cumple lo que estamos buscando y la salida sera True, en caso que no exista sera False porque no existe cadena que cumpla con las condiciones dadas(orden de clases, cardinalidad K).

Notese que preguntar por el (K+x)-esimo elemento se puede ver como preguntar: desde el indice donde me encuetro hasta que indice debo moverme para tener K elementos de Ci, dado que x es la cantidad de elementos de ci hasta el indice actual, y me interesa avanzar k repeticiones de ci, luego en la posicion que aparece dicho elemento habra entonces k repeticions de ci desde el indice actual hasta el cual me movere.

__Complejidad__: El algoritmo realiza 8 iteraciónes, que va de una clase a otra, es entonce O(1), pero lo veremos como 8, dado que para calcular cadenas que cumplen que la cardinalidad de cada clase es (K o K-1) tambien sera O(1) pero en la practica sera mas costoso(mayor constante)


### Función 2:

__input__: int K, cadena A, orden de Clases.

__output__: int: cardinalidad de la subsecuencia donde cada clase tiene cardinalidad k o k-1.

Analogo al algoritmo para calcular cadenas unicamente de tamano K, el procedimiento es el mismo, solo que en este caso tenemos por cada clase dos opciones, que la cardinalidad sea K o que sea K-1, por lo que se tendran que probar todas las premutaciones para ello sigueindo la misma idea del algoritmo, pero ahora se pregunta en cada caso no solo por la posicion (k+x)-esima, sino tambien por otra posicion (k+y)-esima dado que existen nos interesan dos posibilidades: o la clase ci tiene cardinalidad k, o tiene cardinalidad k-1.

__Complejidad__ : en este caso al existir dos posibilidades por cada clase, sera $2 * 2 * 2 *$ ... = $2^8$ posibilidades. Notese que ahora se realizan 256 operaciones, a diferencia de 8 que se realizan en el algoritmo anterior, luego la complejidad es O(1), pero en la practica son 256 iteraciónes, lo cual es mas lento que el algoritmo anterior.

Nota: el costo de preguntar por estas posiciones y valores es O(1) dado que esto estara precalculado, de no estarlo el costo seria n.

### Precálculo 1

Creamos un array que actuará como función donde en todo momento podemos preguntarle el indice del k-esimo elemento de una clase específica.
```python
# indice del k-esimo elemento de la clase1
indice = posicion[clase1][k]
```
Esto se hace recorriendo $A$ y guardando cada indice en la lista asociada a su clase.

Dado que recorrimos cada uno de los elementos de $A$ no puede quedar ningún indice asociado a un elemento sin agregar. Estos indices para cada una de las 8 listas no pueden quedar en orden incorrecto pues implicaría que se llegó en el recorrido primero un indice menor que otro, lo cual es imposible. Luego de terminar el recorrido cada una de las 8 listas tendrán un tamaño de la cantidad de elementos asociada a su clase.

__Complejidad__: es de $O(|A|)$ ya que en un recorrido donde por cada elemento que nos encontremos vamos a agregar su indice asociado a una de las 8 posibles listas. 

### Precálculo 2
Creamos una matriz de $N$ x 8 siendo $|A|=N$ y 8 la cantidad de clases disponibles que actuará como función. Para cada posición i de la matriz por el eje 0 tendremos la cantidad de elementos de cada clase que están en $A$ tal que que tengan una posición menor que i en $A$.

```python
#total de elementos antes del indice k en A de clase1
total = quantity[k][clase1]
```
Vamos a recorrer $A$, y vamos a ir llevando la frecuencia de aparición de los elementos en un array de 8 posiciones (cada vez que nos encontramos un elemento de clase c1, incrementamos la frecuencia de c1 en 1). Además por cada elemento vamos a guardar una copia del array de frecuencias en su indice asociado, representando la cantidad de elementos que han aparecido hasta el momento en $A$. Retornamos la matriz contruida.

Para una clase c1 en el indice k, se tiene que cumplir que `quantity[k][c1]` estan la cantidad de elementos del tipo c1 que hasta ahora k han aparecido en $A$, de no ser así quiere decir que faltó alguno por encontrarse en el recorrido hasta k o se contó uno extra, esto no puede ocurrir ya que solo la frecuencia se incrementa en cada momento que se encuntre un elemento de tipo c1, por lo que una vez que llegue al indice k la frecuencia de c1 va a tener el valor de la cantidad de elementos de tipo c1 antes de k. Esto va a pasar para una de las clases.

__Complejidad__: es de $O(|A|)$ ya que en un recorrido donde por cada elemento que nos encontremos vamos a agregar una lista de 8 elementos al array solución. 


--- 

### Demostración

1. Si no existe ninguna subsecuencia de cardinalidad $K$ (para cada clase) de $A$, entonces no existe subsecuencia de cardinalidad $K_0$ o $K_0-1$ para cada clase en $A$ con $K_0 > K$.

    Veamos esto como contrarecíproco:

    [existe subsecuencia de cardinalidad $K_0$ o $K_0-1$ para cada clase en A, $K_0$ > K] 
    $\Rightarrow$
    [existe subsecuencia de cardinalidad K (para cada clase) de A]

    Si esta implicación se cumple entonces se cumple la que queremos demostrar.

    Asumimos entonces que se cumple la parte izquierda:

    Luego en A existe subsecuencia que cumple con la cardinalidad dada, $K_0 > K$, luego $K_0 >= K +1$, luego $K_0-1 >= K+1-1$, luego $K_0-1>=k$. Como existe subsecuencia en $A$ que cumple la parte izquierda, luego cada clase de la subsecuencia tendra $K_0$ o $K_0-1$ repeticiones, donde ambos son mayores o iguales que $K$, luego si eliminamos elementos convenientemente de la secuencia que cumple estas restricciones entonces llegamos a una subsecuencia donde todas las cardinalidades son de tamano $K$, luego se cumple que exite la subsecuencia con las restricciones de la parte derecha, luego se cumple el planteamiento que queriamos demostrar.

    Notese que el resultado de eliminar elementos de una secuencia resulta en una subsecuencia de la secuencia a la cual le eliminamos elementos, le estamos eliminando elementos a una subsecuencia de A, lo cual resulta en una subsecuencia de una subsecuencia de A que a los efectos es una subsecuencia de A.

2. Análogo a esta demostración podemos decir que si no existen subsecuencias donde cada clase tenga cardinalidad $K$ para un orden específico(orden de las clases), entonces para ese orden específico no existirán subcadenas donde cada elemento tendrá cardinalidad $K_0$ o $K_0-1$ con $K_0>K$. Esta demostracion es un caso específico de la demostracion anterior, en la anterior es para todos los casos de orden, y este para casos específicos.

Con todo lo que tenemos hasta ahora podemos decir que:

- Si existe una subsecuencia de cardinalidad $K$(para todas sus clases), entonces puede existir una de cardinalidad ($K_0$ o $K_0-1$) para cada clase.

- Si no existe subsecuencia de cardinalidad K(para todas sus clases) para una ordenación, entonces para esa ordenación no existen subsecuencias de cardinalidad $K_0$ o $K_0-1$ para cada clase con $K_0>K$.

Entonces si encuentro solución para $K$ me interesa preguntar por un $K_0$ mayor dado que ahi puede estar mi solución general, pero si no existe entonces no hay $K_0$ mayor donde se encuentre nuestra solución general por lo que esa solución estara por debajo de $K$. Esto se puede ver entonces como una busqueda binaria donde mi predicado es (existe solución para $K$ exacto), lo cual es exactamente el output de la __Función 1__.

Demostremos ahora que el $K máximo que puede cumplir con las restricciones es $K = \frac{|A|}{8}$:

Supongamos que exista una subsecuencia que posea una clase con cardinalidad mayor a $\frac{|A|}{8}$, sea esa clase c1, y que cumple con las restricciones de cardinalidad del problema, entonces existe al menos una clase con cardinalidad menor que $\frac{|A|}{8}$, porque de no ser asi entonces todas tienen cardinalidad mayor o igual lo cual implica que la subsecuencia tendra como minimo $7*\frac{|A|}{8} + \frac{|A|}{8} + 1$, dado que hay una clase con cardinalidad $\ge \frac{|A|}{8}+1$, luego no puede ser subsecuencia, luego existe esta clase con cardinalidad menor que  y la diferencia de la misma con la que es mayor a $\frac{|A|}{8}$, es mayor que 1, luego no cumple las restricciones, luego queda demostrado lo que se planteo. Dado que la division entre 8 no debe ser exacta, trabajamos sin perder generacidad con un valor máximo para K mayor que el techo de $\frac{|A|}{8}$, luego nuestro mayor K para el cual trabajamos sera:

 $K = \frac{|A|}{8}+1$.


Luego partiendo desde ese $K$ y realizando la busqueda binaria planteada llegamos a un último $K$, donde se encuentra la solución máxima para subsecuencias con exactamente cardinalidad $K$ cada clase. Se asegura que la busqueda binaria pasara por $K+1$, preguntara si hay solución en $K+1$ para cardinalidades exactas, de esta forma se asegura que no existe solución en $K+2$ (por lo demostrado en \[Demostracion.1\]). Luego una vez llegamos al último $K$ aplicamos el algoritmo para buscar cadenas de $K+1$ o $K$, y aquí encontraremos nuestra solución general, si existe es esta, si no existe es la máxima encontrada en $K$.

En cada iteración por lo demostrado en \[Demostracion.2\] reduciremos la lista de posibles ordenaciones a una lista donde solo estén incluidas las ordenaciones donde se encontró subsecuencia válida para el $K$ mayor analizado.

Luego el algoritmo parte con una complejidad de $8!* 8 * O(log(|A|/8))$, donde cada vez que encontremos un $K$ se reduce la constante factorial(en un primer momento todas las formas de ordenar posibles), y en el último paso del algoritmo tendremos  $256*|L|$ operaciones donde $L$ es la lista con todas las ordenaciones posibles con las que se llego al final.

En la practica el orden es el anterior. En teoria el orden de este algoritmo es O(log(n)).

Precalcular los valores que se necesitan para preguntar en las funciones 1 y 2 tiene un costo de O(n), recorrer la cadena. Luego el costo final de este algoritmo es:

O(n) + O(log(n)) = O(n). Pero en la practica la parte fuerte del algoritmo se calcula en complejidad de O(log(n)).

---

## Tester

Incluimos un tester en nuestro proyecto donde comparamos nuestra solución final con la solución exponencial, ayudandonos a descartar ideas simples cuando estabamos en busca de nuevas soluciones.
```python
# para ejecutar los casos autogenerados
python main.py
```
El tester tiene varios parametros como la cantidad de clases, cantidad de casos, tamaño de cada caso etc. También imprime en pantalla el tiempo mínimo, máximo y promedio de ejecución de los casos.
