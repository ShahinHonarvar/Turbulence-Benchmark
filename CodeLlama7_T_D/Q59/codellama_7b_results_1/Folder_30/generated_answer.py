
def all_left_truncatable_prime(tuple):
    x = tuple[37]
    list = []
    for i in range(2, x):
        if is_prime(i) and left_truncatable_prime(i):
            list.append(i)
    return sorted(list, reverse=True)

def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True


def left_truncatable_prime(n):

    str_n = str(n)

    for i in range(len(str_n)):

        num = int(str_n[:i] + str_n[i+1:]))

        if not is_prime(num):

            return False


    return True
