import random


# This function generates a random list of integers. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, seed):
    if seed != 'default':
        random.seed(seed)
    n = l[0]
    length = 3 if n < 50 else 2 if 50 <= n < 100 else 1 
    result = [
        random.choice(list(range(10, 100)) * 50 + list(range(100, 1000)) * 40 + list(range(1000, 10000)) + list(
            range(10000, 20000))) for _ in range((n + 5) * length)]
    
    random.shuffle(result)
    return tuple(result)