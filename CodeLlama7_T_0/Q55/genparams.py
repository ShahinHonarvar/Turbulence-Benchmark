import random


# This function generates 100 unique random suitable parameter values for the question and writes them to all_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    params = []
    selected_range = [(-10, 10)] * 15 + [(-100, -10)] * 35 + [(10, 100)] * 35 + [
        (-1000, -100)] * 7 + [(100, 1000)] * 8
    p = None
    for a_range in selected_range:
        while p in params or p == None:
            p = random.randint(a_range[0], a_range[1])
        params.append(p)
        
    return params