
def all_left_truncatable_prime(tuple):
    x = tuple[645]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i, x):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_left_truncatable_prime(n, x):
    if n < 2 or n >= x:
        return False

    for i in range(n - 1, 0, -1):
        if not is_prime(i) or i >= x:
            return False

    return True
