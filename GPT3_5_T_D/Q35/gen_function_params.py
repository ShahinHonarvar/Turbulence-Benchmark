import random
import string


# This function generates a random string. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    m, n = random.choices(range(2, 4), k=2)
    extension = random.randint(20, 30)
    x = int(l[0]) + int(l[1]) + extension
    s = ''.join(random.choices(string.ascii_letters, k=x // m))
    s += ''.join(random.choices(string.digits, k=x // m))
    s += ''.join(random.choices('$ % & * + < = > @ ', k=x // n))

    s_l = list(s)
    result = []
    while len(s_l) > 0:
        idx = random.randint(0, len(s_l) - 1)
        result.append(s_l[idx])
        del s_l[idx]

    return ''.join(result)
