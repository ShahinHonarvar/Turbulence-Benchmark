import random
import string


# This function generates a random string. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    x = int(l[1])
    result = []
    if (x // 10) < 2:
        n = 2
    else:
        n = x // 10
    random_num = random.randint(1, 3)
    for _ in range(random_num):
        result += list(''.join(random.choice(string.ascii_letters) for _ in range((n + 1) // 2)))
        result += random.choices(range(0, 5), k=n)
        result += list(''.join(random.choice('a $ i % A & o * e + u < I = O > @ E U') for _ in range((n + 1) // 2)))
    random.shuffle(result)
    s = ''
    for i in result:
        s += str(i)
    return s
