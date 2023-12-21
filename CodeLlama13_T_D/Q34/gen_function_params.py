import random


# This function generates several sets of random sizes and random integers.
# The number of generated integer sets depends on the value of the argument being passed to the function.
# The outputs of this function will be passed to the generated code by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    x = int(l[0])
    result = []
    for _ in range(x):
        length = random.randint(2, 20)
        result.append(set(random.sample(range(-100, 100), length)))

    random.shuffle(result)

    return result
