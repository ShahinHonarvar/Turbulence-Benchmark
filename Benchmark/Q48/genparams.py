import random


# This function generates 80 unique random pairs of suitable parameter values for the question and writes them to
# all_params.txt. Initially, 20 unique rows of manually chosen values were stored in manually_chosen_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    with open(f'Q{q_no}/manually_chosen_params.txt', 'r') as f:
        params = [(int(l.strip('\n').split()[0]), int(l.strip('\n').split()[1])) for l in f.readlines()]

    selected_range = [range(0, 10)] * 10 + [range(10, 100)] * 65 + [range(100, 1000)] * 5
    p0, p1 = 0, 0
    for a_range in selected_range:
        while (p0, p1) in params or p1 <= p0 + 1:
            p0, p1 = random.sample(a_range, k=2)
        params.append((p0, p1))
    
    return params
