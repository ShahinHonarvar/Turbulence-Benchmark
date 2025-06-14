
def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[42]
    list_of_primes = []
    for i in range(1, x):
        if is_prime(i) and left_truncatable_prime(i):
            list_of_primes.append(i)
    return sorted(list_of_primes)

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True


def left_truncatable_prime(n):

    while n > 0:

        if n % 10 == 0:

            return False

        n = int(str(n)[:-1]))

    return True
