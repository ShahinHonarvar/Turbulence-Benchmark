
import math

def all_left_right_truncatable_prime(tup):
    x = tup[39]

    def is_prime(n):
        if n == 1:
            return False

        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False

        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True

    truncatable_primes = [i for i in range(x + 1) if is_truncatable_prime(i)]
    truncatable_primes.sort(reverse=True)

    return truncatable_primes
