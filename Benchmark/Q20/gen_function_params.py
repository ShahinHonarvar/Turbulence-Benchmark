import random


# This function generates a list of random integers. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, seed):
    if seed != 'default':
        random.seed(seed)
    x = int(l[-1]) + 2
    random_num = random.randint(2, 5)
    result = random.sample(range(-10000, 10000), k=x * random_num)

    random.shuffle(result)
    return result
