
def all_right_truncatable_prime(tuple):
    x = tuple[370]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):
    while len(str(n)) > 1:
        n = int(str(n)[0:-1]))
        if not is_prime(n):
            return False

    return True
