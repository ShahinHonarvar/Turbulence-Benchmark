# This scrip generates a random string. The output generated will be passed to
# the generated code by the large language model and the model solution.

import random
import string


def input_generator(l, random_seed):
    random.seed(random_seed)
    x = l[1]
    length = random.randint(100, 200)
    return ''.join(
        random.choices(
            (x * 5) + string.ascii_letters + (x * 5) + string.digits + ' ' * (length // 20) + (x * 5), k=length
        )
    )
