import random


# This function generates a list of random integers. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    x = max(int(l[0]), int(l[1])) + 2
    random_selection = random.randint(0, 1)
    if random_selection:
        return random.choices(range(1, 1020), k=x)
    else:
        return random.sample(range(1, 1020), k=x)
