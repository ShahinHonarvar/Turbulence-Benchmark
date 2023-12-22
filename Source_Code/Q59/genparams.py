import random


# This function generates 100 unique random suitable parameter values for the question and writes them to all_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    params = []
    selected_range = [(0, 10)] * 8 + [(11, 100)] * 72 + [(101, 1001)] * 20
    p = None
    order = None
    for a_range in selected_range:
        option = random.randint(0, 1)
        while (p, order) in params or p is None or order is None:
            p = random.randint(a_range[0], a_range[1])
            order = 'ascending' if option else 'descending'
        params.append((p, order))

    return params
