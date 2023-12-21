import random
import string


# This function generates a random string. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)

    n = l[0]
    if n < 100:
        x = random.randint(10, 20)
    else:
        x = random.randint(5, 10)

    return "".join(
        random.choices(
            string.ascii_letters + string.digits + " " * 10 + string.punctuation,
            k=x + n,
        )
    )
