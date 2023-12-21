
def all_left_truncatable_prime(tuple):
    x = tuple[22]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i, x):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n, x):
    if n < 2 or x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    while n > 1:

        if n % 10 == 0:
            return False

        n = n // 10

    return True
