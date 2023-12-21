def all_left_truncatable_prime(n):
    primes = set(range(3, int(n[0])))
    for i in range(len(n) - 1):
        primes &= set(str(n[i + 1])[1:])
    return sorted(primes)
