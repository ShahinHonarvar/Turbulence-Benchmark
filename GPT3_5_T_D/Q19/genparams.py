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

    idx_selected_range = (
        [range(0, 10)] * 10 + [range(10, 100)] * 60 + [range(100, 1000)] * 10
    )
    divisor_selected_range = (
        [range(-10, 10)] * 10
        + [range(-100, -10)] * 30
        + [range(10, 100)] * 30
        + [range(-1000, -100)] * 5
        + [range(100, 1000)] * 5
    )
    divisor, idx0, idx1 = 0, 0, 0
    for i in range(len(idx_selected_range)):
        while (divisor, idx0, idx1) in params or idx1 <= idx0 or divisor == 0:
            idx0, idx1 = random.sample(idx_selected_range[i], 2)
            divisor = random.choice(divisor_selected_range[i])

        params.append((divisor, idx0, idx1))

    return params
