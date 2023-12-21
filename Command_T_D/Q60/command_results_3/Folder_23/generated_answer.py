
import math

def all_left_right_truncatable_prime(n):
    left_right_truncatable_primes = []
    for i in range(2, int(math.ceil(math.log(n, 2)) + 1)):
        if all(str(k).count('0') == 0 for k in range(i, n, i)):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)
