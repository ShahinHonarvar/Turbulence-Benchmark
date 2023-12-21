import random


# This function generates a list of random integers. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)

    n = l[0]
    if n == 0:
        k = random.randint(1, 4)
        result = list(range(-k, k + 1))
        random.shuffle(result)

        return result

    elif n > 0:
        divs = [i for i in range(1, n + 1) if n % i == 0]
        result = divs + divs
        random.shuffle(result)

        return result

    else:
        n = -n
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        result = divs + divs
        random.shuffle(result)

        return result
    