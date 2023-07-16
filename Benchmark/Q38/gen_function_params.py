import random


# This function generates a list of random objects. The outputs of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, seed):
    if seed != "default":
        random.seed(seed)
    x = int(l[0]) + 2
    if x < 50:
        n = random.randint(2, 10)
    elif 50 <= x < 200:
        n = random.randint(2, 5)
    else:
        n = random.randint(2, 3)
    length = n * x
    result = set(random.sample(range(-10000, 10000), k=length))

    return result
