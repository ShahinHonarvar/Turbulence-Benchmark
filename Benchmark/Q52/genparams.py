import random


# This function generates 100 unique random suitable parameter values for the question and writes them to all_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    params = []
    selected_range = [(3, 10)] * 6 + [(10, 100)] * 64 + [(100, 500)] * 30
    p = 0
    for a_range in selected_range:
        while p in params or p == 0:
            p = random.randint(a_range[0], a_range[1])
        params.append(p)

    return params