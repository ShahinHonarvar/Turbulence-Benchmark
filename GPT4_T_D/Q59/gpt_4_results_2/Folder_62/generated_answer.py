
def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def left_trunc(p):
    if p < 10:
        return is_prime(p)
    else:
        return is_prime(p) and left_trunc(int(str(p)[1:]))


def all_left_truncatable_prime(t):
    x = t[70]
    truncatable_primes = [p for p in range(x) if '0' not in str(p) and left_trunc(p)]
    return sorted(truncatable_primes)
