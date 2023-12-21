import random


# This function generates 100 unique random suitable parameter values for the question and writes them to all_params.txt.
def gen_params(q_no, seed):
    if seed != "default":
        random.seed(seed)
    params = []

    selection_range = (
        [range(-10, 0)] * 5
        + [range(0, 10)] * 5
        + [range(-100, -10)] * 30
        + [range(10, 100)] * 30
        + [range(100, 1001)] * 15
        + [range(-1000, -100)] * 15
    )
    n = None
    for a_range in selection_range:
        while n in params or n is None:
            n = random.choice(a_range)
        params.append(n)

    return params
