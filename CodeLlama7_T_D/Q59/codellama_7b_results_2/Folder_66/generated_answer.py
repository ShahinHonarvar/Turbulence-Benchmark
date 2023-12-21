
def all_left_truncatable_prime(tuple):
    x = tuple[25]
    left_truncatable_primes = []
    for i in range(1, x + 1):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
def is_left_truncatable_prime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
