import random


# This function generates 100 unique random suitable parameter values for the question and writes them to
# all_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    params = []
    selection_range = [range(1, 10)] * 7 + [range(10, 100)] * 63 + [range(100, 200)] * 30
    n = 0
    for a_range in selection_range:
        while n in params or n == 0:
            n = random.choice(a_range)
        params.append(n)
        
    return params