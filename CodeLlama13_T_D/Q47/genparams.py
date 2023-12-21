import random


# This function generates 80 unique rows of 4 random suitable parameter values for the question and writes them to
# all_params.txt. Initially, 20 unique rows of manually chosen values were stored in manually_chosen_params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    with open(f'Q{q_no}/manually_chosen_params.txt', 'r') as f:
        params = [(int(l.strip('\n').split()[0]), int(l.strip('\n').split()[1]), int(l.strip('\n').split()[2]),
                   int(l.strip('\n').split()[3])) for l in f.readlines()[:20]]

    idx_selected_range = [range(0, 10)] * 5 + \
        [range(10, 100)] * 65 + [range(100, 300)] * 10
    lengths_selected_range = [
        range(3, 10)] * 10 + [range(10, 100)] * 60 + [range(100, 300)] * 10
    i, j, m, n = 0, 0, 0, 0
    for k in range(len(idx_selected_range)):
        while (i, j, m, n) in params or j <= i or n <= m or m < 3 or n == 0 or (j - i - 1) < 3 or (j - i - 1) < n:
            i, j = random.sample(idx_selected_range[k], 2)
            m, n = random.sample(lengths_selected_range[k], 2)

        params.append((i, j, m, n))

    return params
