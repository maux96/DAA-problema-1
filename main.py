import colorama

from tester import gen_cases
import naive_solution, ultra_naive_solution

if __name__ == '__main__':
    TOTAL_CASES = 1000
    CLASSES = 3 
    SIZE = 8 

    success_count = 0
    for i,(arr, sol) in enumerate(gen_cases(
            ultra_naive_solution.solution,
            cases=TOTAL_CASES,
            classes=CLASSES,
            size=SIZE)):
        new_solution=naive_solution.solution(arr, CLASSES)
        if new_solution != sol:
            print(f'{colorama.Fore.RED}[X] ({i+1}) ERROR!: {colorama.Fore.RESET} {new_solution}!={sol} {colorama.Fore.RED}, array:{colorama.Fore.RESET} {arr}')
        else:
            print(f"{colorama.Fore.GREEN}[0] ({i+1}) OK! ({new_solution}=={sol}){colorama.Fore.RESET}")
            success_count +=1
    print(f"Results: {success_count}/{TOTAL_CASES} (~{100*(success_count/TOTAL_CASES):.2f}%)")


