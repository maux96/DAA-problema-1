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
## Solucion O($n$) con muy alta constante 
    TODO

### Correctitud
    TODO
### Complejidad
    TODO

----
