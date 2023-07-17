# This scrip generates a random string. The output generated will be passed to
# the generated code by the large language model and the model solution.

import random
import string


def input_generator(l, seed):
    if seed != 'default':
        random.seed(seed)
    length = random.randint(100, 200)
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ' * (length // 20), k=length))