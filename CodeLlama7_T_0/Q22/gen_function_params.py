import random


# This function generates a random integer.
def input_generator(l, random_seed):
    random.seed(random_seed)
    return random.randint(1, 1000)
