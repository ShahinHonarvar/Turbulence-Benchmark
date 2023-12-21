import random


# This function generates 100 unique random suitable parameter values for the question and writes them to all_params.txt.
def gen_params(q_no, seed):
    if seed != "default":
        random.seed(seed)
    params = []
    p0, p1 = 0, None
    while len(params) < 100:
        while (p0, p1) in params or p0 == 0 or p1 == None:
            p0 = random.randint(2, 90)
            option = random.randint(0, 1)
            if option:
                p1 = "ascending"
            else:
                p1 = "descending"

        params.append((p0, p1))

    return params
