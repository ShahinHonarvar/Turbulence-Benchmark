import random
import numpy as np


# This function generates a random 2D matrix. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)

    num = l[0]
    if num < 4:
        num = 4
    elif 4 <= num < 50:
        num //= 2
    elif 50 <= num < 100:
        num //= 4
    elif 100 <= num < 300:
        num //= 8
    elif 300 <= num < 600:
        num //= 16
    else:
        num //= 32

    d1 = random.randint(1, num)
    d2 = random.randint(1, num)
    mat = [[random.randint(-10, 10) for _ in range(d2)] for _ in range(d1)]

    return np.asmatrix(mat)