import random


# This function generates 100 unique random suitable parameter values for the question and writes them to all_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    params = []
    selected_range = [(0, 10)] * 9 + [(10, 100)] * 61 + [(100, 1000)] * 30
    p = 0
    for a_range in selected_range:
        while p in params:
            p = random.randint(a_range[0], a_range[1])
        params.append(p)

    return params