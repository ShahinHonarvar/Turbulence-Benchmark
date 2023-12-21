
from itertools import chain

def all_left_right_truncatable_prime(t):
    x = t[69]

    def is_prime(n):
        if n == 1:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False

        if not is_prime(n):
            return False

        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:i])) or not is_prime(int(str(n)[-i:])):
                return False
        return True

    left_right_truncatable_primes = [i for i in chain(range(x, 1, -1)) if is_truncatable_prime(i)]

    return sorted(left_right_truncatable_primes, reverse=True)
