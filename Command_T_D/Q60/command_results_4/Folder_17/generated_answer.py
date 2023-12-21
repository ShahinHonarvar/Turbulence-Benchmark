
import math

def all_left_right_truncatable_prime(lim):
    return [n for n in range(2, int(math.ceil(10**9 ** 0.5)) + 1) if all(n % d != 0 for d in range(2, int(math.ceil(10**9 ** 0.5)) + 1) if n % d == 0)]
