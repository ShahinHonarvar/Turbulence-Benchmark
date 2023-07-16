import random
import string


# This function generates 75 unique random pairs of suitable parameter values for the question and writes them to
# params.txt. Initially, 25 unique rows of manually chosen values were stored in params.txt.
def gen_params(q_no, seed):
    if seed != 'default':
        random.seed(seed)
    with open(f'Q{q_no}/manually_chosen_params.txt', 'r') as f:
        params = [(l[0], l[1]) for line in f.readlines()[:25] if (l := line.split())]
    char0, char1 = ' ', ' '
    while len(params) < 100:
        while (char0, char1) in params:
            char0, char1 = random.choices(string.ascii_letters + string.digits + ' ' * 5, k=2)

        params.append((char0, char1))

    return params
