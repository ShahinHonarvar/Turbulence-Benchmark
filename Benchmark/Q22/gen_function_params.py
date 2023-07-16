import random


# This function generates a random integer.
def input_generator(l, seed):
    if seed != 'default':
        random.seed(seed)
    return random.randint(1, 1000)
