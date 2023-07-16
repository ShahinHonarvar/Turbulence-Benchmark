# This scrip generates a random string which may include a palindrome sequence. The output generated will be passed to
# the generated code by the large language model and the model solution.

import random
import string


def input_generator(l, seed):
    if seed != "default":
        random.seed(seed)
    n = int(l[1])
    if n < 100:
        coef = random.randint(1, 10)
    else:
        coef = random.randint(1, 3)

    length = (n + 2) * coef
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

    return result
