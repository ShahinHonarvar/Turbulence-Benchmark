
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    x = tup[96]
    primes = []

    for i in range(x):
        if is_right_truncatable(i):
            primes.append(i)

    return sorted(primes, reverse=True)
