import random


# This function generates 90 unique random suitable parameter value for the question and writes them to
# all_params.txt. Initially, 10 unique rows of manually chosen values were stored in manually_chosen_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    with open(f'Q{q_no}/manually_chosen_params.txt', 'r') as f:
        params = [int(l.strip('\n').split()[0]) for l in f.readlines()[:13]]
    selected_range = [range(11, 100)] * 65 + [range(100, 500)] * 26
    p = 0
    for a_range in selected_range:
        while p in params or p == 0:
            p = random.choice(a_range)
        params.append(p)

    return params
