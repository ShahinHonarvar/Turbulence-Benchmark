import random


# This function generates a list of random integers. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, seed):
    if seed != 'default':
        random.seed(seed)
    if int(l[0]) == 0:
        x = 2
    else:
        x = int(l[0])
    result = []
    random_num = random.randint(2, 5)
    for _ in range(random_num):
        random_selection = random.randint(0, 1)
        if random_selection:
            result += random.choices(range(1, 1000), k=x)
        else:
            result += random.sample(range(1, 1000), x)

    random.shuffle(result)
    return result
