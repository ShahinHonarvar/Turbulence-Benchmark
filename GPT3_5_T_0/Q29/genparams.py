import random


# This function generates 100 unique random pairs of suitable parameter values for the question and writes them to
# all_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    params = []
    selected_range = [range(0, 10)] * 10 + [range(10, 100)] * 70 + [range(100, 1000)] * 20
    p0, p1 = 0, 0
    for a_range in selected_range:
        while (p0, p1) in params:
            p0, p1 = random.sample(a_range, k=2)
        params.append((p0, p1))

    return params
