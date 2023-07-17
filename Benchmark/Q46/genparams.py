import random


# This function generates 100 unique sets of 3 random suitable parameter values for the question and writes them to
# all_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    params = []
    selected_range = [range(0, 10)] * 10 + [range(10, 100)] * 70 + [range(100, 1000)] * 20
    p0, p1, p2 = None, None, None
    for a_range in selected_range:
        while (p0, p1, p2) in params or p0 is None or p1 is None or p2 is None:
            p0, p1, p2 = random.sample(a_range, k=3)
        params.append((p0, p1, p2))

    return params
