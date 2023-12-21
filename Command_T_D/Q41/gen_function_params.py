import random
import string


# This function generates two lists of random objects. The outputs of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    x = int(l[1]) + 2
    result0 = []
    result1 = []
    result0 += list(''.join(random.choice(string.ascii_letters) for _ in range(x)))
    result0 += random.choices(range(-1000, 1000), k=(x))
    result0 += list(''.join(random.choice('$%&*+<=>@') for _ in range(x)))
    result1 += list(''.join(random.choice(string.ascii_letters) for _ in range(x)))
    result1 += random.choices(range(-1000, 1000), k=(x))
    result1 += list(''.join(random.choice('$%&*+<=>@') for _ in range(x)))
      
    random.shuffle(result0)
    random.shuffle(result1)

    return result0, result1
