import random


# This function generates 100 unique random sets of suitable parameter values for the question and writes them to
# all_params.txt.
def gen_params(q_no, seed):
    params = []
    selected_range = (
        [range(0, 10)] * 10 + [range(10, 100)] * 70 + [range(100, 1000)] * 20
    )
    p0, p1, p2 = 0, 0, None
    for a_range in selected_range:
        while (p0, p1, p2) in params or p1 < p0 or p2 is None:
            p0, p1 = random.choices(a_range, k=2)
            option = random.randint(0, 1)
            if option:
                p2 = "ascending"
            else:
                p2 = "descending"
        params.append((p0, p1, p2))

    return params
