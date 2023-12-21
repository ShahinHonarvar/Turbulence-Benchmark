
from math import isqrt
def is_prime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tuple_of_integers):
    def truncate(n):
        str_n = str(n)
        return [int(str_n[:i]) for i in range(1, len(str_n) + 1)] + [int(str_n[i:]) for i in range(len(str_n))]

    primes = []
    for x in tuple_of_integers:
        if x < 11:
            continue
        for num in range(x, 10, -1):
            if all(is_prime(i) for i in truncate(num)):
                primes.append(num)

    primes.sort(reverse=True)
    return primes
