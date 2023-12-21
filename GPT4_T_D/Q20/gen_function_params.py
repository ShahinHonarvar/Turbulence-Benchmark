import random


# This function generates a list of random integers. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    x = int(l[-1]) + 2
    result = random.sample(range(-1000, 1000), k=x)

    return result
