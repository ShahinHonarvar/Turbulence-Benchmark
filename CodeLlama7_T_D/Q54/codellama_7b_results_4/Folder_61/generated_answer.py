
def all_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[3]
    list_of_right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            list_of_right_truncatable_primes.append(i)
    return sorted(list_of_right_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(int(str(n)[:-1]))):
            return False

        n = int(str(n)[:-1]))

    return True
