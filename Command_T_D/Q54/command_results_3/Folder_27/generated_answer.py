import math
def all_right_truncatable_prime(n):
    n = (int(n),)
    x = n[0]
    return [n for n in range(3, int(math.ceil(x ** .5)) + 1, 2) if all(n % d != 0 for d in range(3, int(math.ceil(n ** .5)) + 1, 2))]
