
def all_left_truncatable_prime(tuple):
    x = tuple[55]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i, x)):
            list.append(i)
    return sorted(list)

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_left_truncatable_prime(n, x):

    while n > 0 and n < x:

        if not is_prime(int(str(n)[:-1]))):

            return False

        else:

            n = int(str(n)[:-1]))

    if n == 0 or n == x:

        return True

    else:

        return False
