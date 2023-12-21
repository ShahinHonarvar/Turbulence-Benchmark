import random


# This function generates a list of random objects. The outputs of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    x = int(l[0]) + 20
    result = set(random.sample(range(-10000, 10000), k=x))

    return result
