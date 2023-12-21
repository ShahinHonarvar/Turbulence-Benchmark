import random
import string


# This function generates a random string. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    x = l[0]
    if x < 30:
        num = random.randint(2, 3)
        length = x * num
    elif 30 <= x <= 60:
        num = random.randint(10, 30)
        length = x + num
    elif 60 < x <= 80:
        num = random.randint(5, 10)
        length = x + num
    else:
        length = x + 1

    return ''.join(random.sample(string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~", k=length))