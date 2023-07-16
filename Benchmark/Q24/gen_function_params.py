import random


# This function generates a random positive integer. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, seed):
    if seed != 'default':
        random.seed(seed)
    x = int(l[-1]) + 2
    if x == 0:
        x = 1
    elif x < 0:
        x = -x
    return random.randint(1, x * 10)
