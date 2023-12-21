
def all_right_truncatable_prime(tuple):
    x = tuple[69]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i, x)):
            list.append(i)
    return sorted(list, reverse=True)

def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True


def is_right_truncatable_prime(n, x):

    if n < 2 or n >= x:

        return False


    while n > 9:

        n = int(str(n)[:-1])

    if n == 7 or n == 11:

        return True


    return False
