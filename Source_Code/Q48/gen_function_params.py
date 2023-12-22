import random


# This function generates a list of random integers. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    idx0, idx1 = int(l[0]), int(l[1])
    num = idx1 - idx0 - 1
    middle = random.sample(range(idx0 + 1, idx1 * 2), k=num)
    if not middle:
        middle.append(idx0 + 1)
    middle.sort()
    prefix = list(range(0, idx0 + 1))
    suffix = random.sample(range(middle[-1] + 1, (middle[-1] + 1) * 2), k=(((middle[-1] * 2) - middle[-1] + 1) + 2) // 2)
    suffix.sort()

    result = prefix + middle + suffix
    result = list(set(result))
    result.sort()

    return tuple(result)