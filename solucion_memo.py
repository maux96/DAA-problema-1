import itertools

def permutations(class_count = 3):
    return itertools.permutations([ i for i in range(1,class_count+1)])

def get_matrices(A: list[int], class_count):
    mat: list[list[int]] = [[] for _ in range(class_count)] 
    quantity_mat = []
    frec = [0] * class_count
    for i in range(len(A)):
        mat[A[i]-1].append(i)

        current_quantitys = [0] *class_count
        for j in range(class_count):
            current_quantitys[j]=frec[j]
        quantity_mat.append( current_quantitys)

        frec[A[i]-1]+=1

    return mat, quantity_mat

def calc(A,matrices,perm,init_pos,k):
    positional_matrix, quantity_matrix = matrices

    if len(perm)==0:
        return 0, True

    current_class = perm[0] 

    res1, is_valid1 = 0,False
    res2, is_valid2 = 0,False

    values_before=quantity_matrix[init_pos][current_class-1]


    if k==1 and len(positional_matrix[current_class-1])==0:
        return 0, True

    #caso k
    if values_before + k <= len(positional_matrix[current_class-1]) :
        index_k = positional_matrix[current_class-1][values_before+k-1]   
        res1, is_valid1 = calc(A,matrices,perm[1:],index_k,k)

    #caso k-1
    if values_before+k>1 and\
          values_before + k-1 <= len(positional_matrix[current_class-1]) :
        index_k_1 = positional_matrix[current_class-1][values_before+k-1-1]   
        res2, is_valid2 = calc(A,matrices,perm[1:],index_k_1,k)


    if is_valid1 and is_valid2:
        return max(k+res1,(k-1)+res2), True
    elif is_valid1:
        return k+res1, True
    elif is_valid2:
        return k-1+res2, True

    return 0, False 


def solution( A: list[int], class_count=3):
    k= len(A) // class_count +1
    better_solution = 0
    matrices= get_matrices(A,class_count)

    while k > 0:
        is_someone_valid = False
        for p in permutations(class_count):
            sol,was_valid=calc(A,matrices,p,0,k)
            is_someone_valid |=  was_valid
            better_solution = max(sol,better_solution) if was_valid else better_solution
        if is_someone_valid:
            break

        k-=1
    return better_solution


if __name__ =='__main__':
    A= [1,2,3,4,1,2,3,4]
    #import tester
    #A = tester.gen_random_case(300,8) 
    print(solution(A,4))
    #print(get_position_matrix(A,4))

