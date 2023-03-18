# O(n)
from colorama.ansi import clear_screen


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
    F = [i for i in F]
    return max(F) - min(F) <= 1


def _solution(A: list[int],classes: int, sol: list[list[int]]):
    if len(A)!= 0 and verify(A, classes):
        sol.append(A) 
        return

    for i in range(len(A)):
        _solution(A[:i]+A[i+1:],classes, sol)


def solution(A: list[int],CLASSES=3) -> int:
    sol=[]
    _solution(A, CLASSES,sol )
    M = 0
    index_M = 0
    for i,x in enumerate(sol):
        if len(x) > M:
            M=len(x)
            index_M = i

    return len(sol[index_M])


def main():
    A1 = [1,1,2,2,3,2,3,3,3,1,1,1,3,3,2,2]
    A2 = [1,1,1,1,1,2,2,2]
    sol=[]

    _solution(A2,sol)
    
    M = 0
    index_M = 0
    for i,x in enumerate(sol):
        if len(x) > M:
            M=len(x)
            index_M = i

    print(len(sol[index_M])) 

    #print("\n".join(map(str,sol)),"\n")
    


if __name__ == '__main__':
    main()

