import random


# This function generates 100 unique random pairs of suitable parameter values for the question and writes them to
# all_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    params = []
    selected_range = [range(-10, 10)] * 5 + [range(1, 10)] * 25 + [range(-100, -10)] * 5 + [range(-100, 100)] * 5 + [
        range(10, 100)] * 30 + [range(-1000, -100)] * 5 + [range(-1000, 1000)] * 5 + [range(100, 1000)] * 20
    p0, p1 = 0, 0
    for a_range in selected_range:
        while (p0, p1) in params or p1 <= p0:
            p0, p1 = random.sample(a_range, 2)
        params.append((p0, p1))

    return params
