import random


# This function generates a list of random integers. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    result = []
    random_selection = random.randint(0, 1)
    random_k = random.randint(2, 10)
    if random_selection:
        result = random.choices(list(range(-1000, 1000)) + list(range(-10, 10)) + list(range(-100, 100)), k=random_k)
    else:
        result = random.sample(list(range(-1000, 1000)) + list(range(-10, 10)) + list(range(-100, 100)), k=random_k)
    
    return result
