# O(n)
def verify(A: list[int], classes ):
    F = [0]*classes
    for i,n in enumerate(A):
        if F[n-1]!=0 and A[i-1]!=n:
            # Si ya se encontro la clase n y el anterior no es la clase n
            # entonces no se cumple la restriccion del problema
            return False
        F[n-1]+=1

    # Si entre todas las clases hay solo una diferencia de cardinalidad de 1 a  
    # lo sumo, entonces es verdadero
    return max(F) - min(F) <= 1

#O(n!)
def _solution_old(A: list[int],k: int,current_sol: list[int],classes: int):

    max_length = 0 

    for i in range(k,len(A)):
        current_sol.append(A[i])
        max_length = max(_solution(A,i+1,current_sol,classes),max_length)
        current_sol.pop()

    if verify(current_sol, classes):
        max_length = max(len(current_sol),max_length)

    return max_length 

#
def _solution(A: list[int],k: int, posible_solution: list[int], classes: int):
    if k == len(A):
        return len(posible_solution) if verify(posible_solution, classes) else 0

    value_not_set = _solution(A,k+1,posible_solution,classes)

    posible_solution.append(A[k]) 
    value_set =_solution(A,k+1,posible_solution,classes)
    posible_solution.pop()

    return max(value_not_set,value_set)

def solution(A, classes):
    return _solution(A, 0, [], classes) 

    

def solution_old(A: list[int],CLASSES=3) -> int:
    return _solution_old(A, 0,[], CLASSES ) 


if __name__ == '__main__':
    from tester import gen_random_case
        
    arr=gen_random_case(20,8)
    print(arr)
    print(solution_2(arr,8))

