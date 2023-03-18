import random
from typing import Callable 


def gen_cases(solver: Callable[[list[int], int] ,int], cases = 500, classes=8, size=5):

    for _ in range(cases):
        array = gen_random_case(size,classes)
        sol = solver(array,classes)
        yield array, sol 

def gen_random_case(size,class_count):
    return [ random.randint(1,class_count) for _ in range(size) ]

