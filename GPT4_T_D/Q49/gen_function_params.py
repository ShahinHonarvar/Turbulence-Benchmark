import random


# This function generates a list of random binary strings. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    length = random.randint(1, 1000)
    result = ''.join(random.choices(['0', '1'], k=length))
    if result[0] == '0':
        result = '1' + result[1:]
    return result