import itertools

def permutations(class_count = 3):
    return itertools.permutations([ i for i in range(1,class_count+1)])

def calc(A,perm,init_pos,k):
    best_recursive_solution = 0
    current_len = 0 
    last = init_pos 
    was_valid = True 
    for class_index,current_class in enumerate(perm):
        total = 0
        last_last_position = 0
        for i in range(last,len(A)):
            if A[i] == current_class:
                total+=1
                last_last_position = last
                last = i
                if total == k:
                    break
        if total==k:
            val, is_valid = calc(A,perm[class_index+1:],last_last_position,k)
            if is_valid:
                best_recursive_solution = max(best_recursive_solution, total-1+val)
            current_len += total 
        elif total==k-1:
            current_len+=total
        else: 
            was_valid = False 
            break 

    return max(
        current_len if was_valid else 0,
        best_recursive_solution 
    ), was_valid or best_recursive_solution !=0 

def solution( A: list[int], class_count=3):
    k= len(A) // class_count +1
    better_solution = 0

    while k > 0:
        for p in permutations(class_count):
            sol,was_valid=calc(A,p,0,k)
            better_solution = max(sol,better_solution) if was_valid else better_solution
        k-=1
    return better_solution


if __name__ =='__main__':
    import tester
    #case = tester.gen_random_case(300,8)
    case = [i for i in range(1,9) for _ in range(10)]
    #print(case)
    #print(solution(case,8))
    print(solution(case,8))
