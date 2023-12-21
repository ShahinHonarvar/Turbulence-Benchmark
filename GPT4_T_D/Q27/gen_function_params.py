# This scrip generates a random list. The output generated will be passed to the generated code by the large language model and the model solution.

import random
import string


def input_generator(l, random_seed):
    random.seed(random_seed)
    n = int(l[1])
    length = n + 10
    result = []
    for i in range(length):
        option = random.randint(0, 3)
        if option == 0:
            i = random.choice(string.ascii_letters)
        elif option == 1:
            i = random.choice(range(0, 100))
        elif option == 2:
            i = round(random.uniform(0, 1000), 2)
        else:
            i = ''.join(random.choices(string.ascii_letters + string.digits, k=2))

        result.append(i)

    random.shuffle(result)
    result.append(element)

    return result








# This scrip generates a random list. The output generated will be passed to the generated code by the large language model and the model solution.



import random
import string


def input_generator(l, random_seed):
    random.seed(random_seed)
    element, idx = l[0], int(l[1]) 
    length = idx + 10
    result = []
    for i in range(length):
        option = random.randint(0, 4)
        if option == 0:
            i = random.choice(string.ascii_letters)
        elif option == 1:
            i = random.choice(range(0, 100))
        elif option == 2:
            i = round(random.uniform(0, 1000), 2)
        elif option == 3:
            i = random.choices(string.ascii_letters + string.digits, k=2)
        else:
            i = {random.choice(string.ascii_letters): random.choice(range(0, 1000))}

        result.append(i)
        result.append(element)

    random.shuffle(result)

    return result
