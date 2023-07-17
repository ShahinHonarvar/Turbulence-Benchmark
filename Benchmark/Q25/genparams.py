import random


# This function generates 100 unique random pairs of suitable parameter values for the question and writes them to
# all_params.txt.
def gen_params(q_no, seed):
    if seed != "default":
        random.seed(seed)
    selected_range = (
        [range(0, 10)] * 10 + [range(10, 100)] * 70 + [range(100, 1000)] * 20
    )
    i, j = None, 0
    params = []
    for a_range in selected_range:
        while (i, j) in params or i is None:
            option = random.randint(1, 3)
            if option == 1:
                i = random.choice(a_range)
            elif option == 2:
                i = round(random.uniform(0, 1000), 2)
            else:
                i = [random.choice(a_range), random.choice(a_range)]

            j = random.choice(a_range)

        params.append((i, j))

    return params
