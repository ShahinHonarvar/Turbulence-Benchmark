# This script generates a random string. The output generated will be passed to
# the generated code by the large language model and the model solution.

import random
import string


def input_generator(l, random_seed):
    random.seed(random_seed)
    return ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation + ' ', k=l[-1] + 3))
