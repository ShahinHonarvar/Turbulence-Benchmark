import random


# This function generates 100 unique rows of 3 suitable parameter values for the question and writes them to
# all_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    params = []
    for i in range(3, 8):
        for j in range(0, 10):
            for k in range(i - 1, 10):
                if -2 <= k - j - i <= 1:
                    params.append((i, j, k))
                if i < 5 and (i == k - j - 2 or i == k - j - 3):
                    params.append((i, j, k))

    return random.sample(params, k=100)