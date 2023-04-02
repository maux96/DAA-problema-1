import itertools

def permutations(class_count = 3):
    return itertools.permutations([ i for i in range(1,class_count+1)])

# precalculo 1 y 2
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

#funcion 1
def exist_solution(A, matrices, order,k):
    positional_matrix, quantity_matrix = matrices

    last_index = 0
    for current_class in order: 
        values_before=quantity_matrix[last_index][current_class-1]
        
        if values_before + k > len(positional_matrix[current_class-1]) :
            return False

        last_index = positional_matrix[current_class-1][values_before+k-1]   

    return True

# funcion 2
def calc(A,matrices,perm,init_pos,k):
    positional_matrix, quantity_matrix = matrices

    if len(perm)==0:
        return 0, True

    current_class = perm[0] 
    if (k==1 and len(positional_matrix[current_class-1])==0):
        return 0, True

    res1, is_valid1 = 0,False
    res2, is_valid2 = 0,False

    values_before=quantity_matrix[init_pos][current_class-1]

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


def solution( A: list[int], class_count):
    
    matrices= get_matrices(A,class_count)

    bottom,top  = 1,min(matrices[1][len(A)-1])+2
    middle= (bottom+top) // 2

    perms= list(permutations(class_count))
    while bottom<top:
        middle= (bottom+top) // 2
        is_someone_valid = False
        new_perms = []

        for perm in perms:
            if exist_solution(A,matrices,perm,middle):
                new_perms.append(perm)
                is_someone_valid = True

        if is_someone_valid:
            bottom = middle+1
            top = top
            perms = new_perms
        else:
            bottom =bottom 
            top =middle-1
    

    best_solution = 0

    for perm in perms:
        first=calc(A,matrices,perm,0,bottom+1)[0]
        second=calc(A,matrices,perm,0,bottom)[0]
        best_solution= max(
            first,
            second,
            best_solution
        )

    return best_solution


     


if __name__ =='__main__':
    import tester, time


    A = tester.gen_random_case(10_000_000,8) 
    start_time = time.time()

    sol = solution(A,8)
    print("solution",sol)
    current_time = time.time() - start_time
    print(f"time:{current_time:.5f}")

