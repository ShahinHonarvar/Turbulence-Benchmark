
def all_right_truncatable_prime(tuple):
    x = tuple[175]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i, x):
            list.append(i)
    return sorted(list)

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True


def is_right_truncatable_prime(n, x):

    while n > 0 and n < x:

        n = int(str(n)[:-1])

    if n == 0 or n == x:

        return True

    else:

        return False
