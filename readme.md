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

## Solución peor fuerza bruta ($O(2^n)$)

Va a consistir en construir todas las posibles subsecuencias de A y verificar que cumplan las restricciones, nos quedamos con la mayor de las cardinalidades de las subsecuencias que cumplen las restricciones. Esta solución debido a que es muy intuitiva y facil de demostrar, la usamos para "testear" soluciones mas complejas que proximamente presentamos.

### Correctitud
Dado que estamos construyendo todas las subsecuencias, la subsecuencia con el mayor tamaño y sea válida la vamos a encontrar en algún punto y vamos guardar satisfactoriamente su valor. Una vez encontrada este valor no va a variar ya que encontar una mejor seria la única forma de cambiar el valor pero como es la subsecuencia de mayor tamaño esta no se va a encontrar una mejor. Luego este algoritmo nos da una solución correcta.

### Complejidad
    TODO


----
## Solución 
Dada la cadena A, vamos a asumir que es una subsecuencia valida, por tanto se cumplirá que $\forall i,j$ entre 1 y 8, $| |C_i| - |C_j| | \le 1$ siendo $C_i, C_j$ todas las posibles clases.

La mayor cardinalidad posible de cualquiera de los conjuntos de elementos de una misma clase pertenecientes a la subsecuencia solución T tiene que ser $k=\frac{|A|}{8}+1$ por lo que   empezaremos asumiendo que en $T$ las clases $C_i$ asociadas a este cumplen que $k-1\le|C_i|\le k$.

Entonces vamos a ver si para una cardinalidad $k$ (empezando por la mayor posible $k$) se cumple que existe una subsecuencia $T$ válida. De no existir reducimos el valor de $k$ y probamos si existe una subsecuencia para el nuevo valor tal que que cumpla las restricciones. Esto lo vamos a hacer varias veces hasta que para un $k$ se cumpla que existe $T$ válida. Luego terminamos el algoritmo y retornamos el tamaño de T que será maximo. 


TODO: ALGORITMO PARA ENCONTRAR EL K VALIDO!

Vamos a iterar por todas las permutaciones de posibles ordenes en los que pueden aparecer las clases en la subsecuencia solucion T, por cada uno de los posibles ordenes, vamos a tratar de construir T (asumiendo que se cumple  $| |C_i| - |C_j| | \le 1$), si $\forall i, |C_i|$


### Correctitud
    TODO
### Complejidad
    TODO

----
