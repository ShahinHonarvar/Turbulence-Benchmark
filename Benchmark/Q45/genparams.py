import random


# This function generates 100 unique rows of 3 suitable parameter values for the question and writes them to
# all_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    params = []
    for i in range(3, 10):
        for j in range(0, 10):
            for k in range(i - 1, 10):
                if i <= k - j + 1:
                    params.append((i, j, k))

    return random.sample(params, k=100)