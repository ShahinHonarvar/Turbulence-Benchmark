import random


# This function generates a random positive integer. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    n = int(l[-1])
    x = (n + 1) * 5 if n < 100 else (n + 1) * 2
    return random.randint(1, x)
