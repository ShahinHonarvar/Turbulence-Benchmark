import random
import numpy as np


# This function generates a random 2D matrix. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def matrix_generator(d1, d2, s):
    mat = []
    total = 0
    for _ in range(d1 - 1):
        row = [random.randint(-100, 101) for _ in range(d2)]
        random.shuffle(row)
        total += sum(row)
        mat.append(row)

    remainder = s - total
    last_row = []
    sum_value = 0

    for _ in range(d2 - 1):
        num = random.randint(-100, 100)
        last_row.append(num)
        sum_value += num

    last_row.append(remainder - sum_value)
    random.shuffle(last_row)
    mat.append(last_row)

    return mat


def input_generator(l, random_seed):
    random.seed(random_seed)

    s = l[0]
    d1, d2 = random.choices(range(2, 6), k=2)
    mat0 = matrix_generator(d1, d2, s)
    mat1 = matrix_generator(d1, d2, s)
    if d1 < 100 and d2 < 100:
        iteration_num = random.randint(1, 3)
        option = random.randint(0, 1)
        length = d1 if option else d2
        m = np.concatenate((mat0, mat1), axis=option)
        for _ in range(iteration_num):
            mat = matrix_generator(d1, d2, s)
            a = [random.randint(-10, 11) for _ in range(length)]
            if option:
                a = np.asarray([a])
                m = np.concatenate((m, mat, a.T), axis=option)
            else:
                m = np.concatenate((m, mat, [a]), axis=option)
    else:
        a0 = [random.randint(-10, 11) for _ in range(d2)]
        a1 = [random.randint(-10, 11) for _ in range(d2)]
        m = np.concatenate(([a0], mat0, [a1]), axis=0)

    return np.asmatrix(m)
