import random
 

# This function generates a random list of integers. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    n = l[0]
    result = random.choices(range(10, 1000), k=n+10)
 
    return tuple(result)