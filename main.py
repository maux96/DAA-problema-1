import colorama

from tester import gen_cases
import naive_solution,n_solution
import asd

import time

   
def compare_and_print(solver, solver_to_eval, cases=10, classes=8, size=10):
    success_count = 0
    time_ = 0
    for i,(arr, sol) in enumerate(gen_cases(
            solver,
            cases=cases,
            classes=classes,
            size=size)):
        start_time = time.time()
        new_solution=solver_to_eval(arr, classes)
        time_ += time.time() - start_time
        if new_solution != sol:
            print(f'{colorama.Fore.RED}[{i+1}] ERROR!: {colorama.Fore.RESET} {new_solution}!={sol} {colorama.Fore.RED}, array:{colorama.Fore.RESET} {arr}')
        else:
            print(f"{colorama.Fore.GREEN}[{i+1}] OK! ({new_solution}=={sol})  array:{colorama.Fore.RESET} {arr}")
            success_count +=1
    print(f"Results: {success_count}/{cases} (~{100*(success_count/cases):.2f}%)")
    print(f"Mean time: {(time_/cases):.5f}s")


if __name__ == '__main__':
    TOTAL_CASES =10
    CLASSES = 8 
    SIZE = 15 
    #for i in range(3,8):
    compare_and_print(
        naive_solution.solution,
        n_solution.solution_2,
        cases=TOTAL_CASES,
        classes=CLASSES,#i,
        size=SIZE
    )
        #input('press enter to continue...')

