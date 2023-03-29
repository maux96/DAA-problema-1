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
    TODO


----
## Solución 
Dada la cadena A, vamos a asumir que es una subsecuencia valida, por tanto se cumplirá que $\forall i,j$ entre 1 y 8, $| |C_i| - |C_j| | \le 1$ siendo $C_i, C_j$ todas las posibles clases.

La mayor cardinalidad posible de cualquiera de los conjuntos de elementos de una misma clase pertenecientes a la subsecuencia solución T tiene que ser $k=\frac{|A|}{8}+1$ por lo que   empezaremos asumiendo que en $T$ las clases $C_i$ asociadas a este cumplen que $k-1\le|C_i|\le k$.

Entonces vamos a ver si para una cardinalidad $k$ (empezando por la mayor posible $k=\frac{|A|}{8}+1$) se cumple que existe una subsecuencia $T$ válida. De no existir reducimos el valor de $k$ y probamos si existe una subsecuencia para el nuevo valor tal que que cumpla las restricciones. Esto lo vamos a hacer varias veces hasta que para un $k$ se cumpla que existe $T$ válida. Luego terminamos el algoritmo y retornamos el tamaño de T que será maximo. 

Por cada $k$ es necesario analizar A para ver si esta satisface la restricción de las cardinalidades. Vamos a seleccionar un orden en que van a aparecer las clases, este orden lo podemos definir como una permutación de las posibles clases. Seleccionado el orden vamos a analizar A (en un principio) recorriendolo y asumiendo que vamos a ir encontrando desde el inicio hasta el final los elementos en forma de la subsecuencia T buscada en el orden seleccionado. Esto se lleva a cabo contando la cantidad de elementos de cada conjunto hasta que tengan el actual valor de $k$ o $k-1$ y pasamos a contar la proxima clase según el orden establecido donde nos quedamos en A después de terminar de contar la clase anterior. Si en algún momento no es válida la cadena porque encontró una clase que su conjunto tenía menos de $k-1$ elementos podemos concluir que para el orden actual, no existe subsecuencia donde para cada una de las clases, sus conjuntos asociados no tienen todos cardinalidad $k$ o $k-1$. 

Si encontramos una subsecuencia $T$ para un $k_0$ entonces no es necesario evaluar todos los $k< k_0$ y simplemente retornaríamos la mayor cardinalidad de las subsecuencias T encontradas (que se fueron construyendo basadas en permutaciones o ordenes de las clases disponibles) para $k=k_0$ como respuesta a nuestro problema.



### Correctitud
    TODO
### Complejidad
    TODO

----
