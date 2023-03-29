import colorama

from tester import gen_cases
import naive_solution, polynomial_solution, polynomial_memo_solution, polynomial_memo_solution_binary_search

import time

   
def compare_and_print(solver, solver_to_eval, cases=10, classes=8, size=10):
    success_count = 0
    time_ = 0
    max_time_ = 0
    min_time_ = 1e9 
    for i,(arr, sol) in enumerate(gen_cases(
            solver,
            cases=cases,
            classes=classes,
            size=size)):
        start_time = time.time()
        new_solution=solver_to_eval(arr, classes)
        current_time = time.time() - start_time
        max_time_ = max(max_time_,current_time)
        min_time_ = min(min_time_,current_time)
        time_ += current_time 
        if new_solution != sol:
            print(f'{colorama.Fore.RED}[{i+1}] ERROR!: {colorama.Fore.RESET} {new_solution}!={sol} {colorama.Fore.RED}, array:{colorama.Fore.RESET} {arr}')
        else:
            print(f"{colorama.Fore.GREEN}[{i+1}] OK! ({new_solution}=={sol})  array:{colorama.Fore.RESET} {arr}")
            success_count +=1
    print(f"Results: {success_count}/{cases} (~{100*(success_count/cases):.2f}%)")
    print(f"Min time: {min_time_:.5f}s")
    print(f"Mean time: {(time_/cases):.5f}s")
    print(f"Max time: {max_time_:.5f}s")


if __name__ == '__main__':
    TOTAL_CASES =1000
    CLASSES = 8 
    SIZE = 15 

    compare_and_print(
        naive_solution.solution,
        #polynomial_memo_solution.solution,
        polynomial_memo_solution_binary_search.solution,
        cases=TOTAL_CASES,
        classes=CLASSES,#i,
        size=SIZE
    )

