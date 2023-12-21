import random


# This function generates 80 unique rows of 3 random suitable parameter values for the question and writes them to
# all_params.txt. Initially, 20 unique rows of manually chosen values were stored in manually_chosen_params.txt.
def gen_params(q_no, seed):
    if seed != "default":
        random.seed(seed)
    with open(f"Q{q_no}/manually_chosen_params.txt", "r") as f:
        params = [
            (
                int(l.strip("\n").split()[0]),
                int(l.strip("\n").split()[1]),
                int(l.strip("\n").split()[2]),
            )
            for l in f.readlines()[:20]
        ]

    n_th, idx0, idx1 = 0, 0, 0
    while len(params) < 100:
        while (
            (n_th, idx0, idx1) in params
            or idx1 <= idx0
            or idx1 - idx0 + 1 < n_th
            or n_th == 0
        ):
            idx0, idx1 = random.sample(range(0, 90), 2)
            n_th = random.randint(4, 20)
        params.append((n_th, idx0, idx1))

    return params
