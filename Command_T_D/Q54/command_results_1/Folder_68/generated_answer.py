def all_right_truncatable_prime(n):
    primes = []
    for p in range(2, n[0] + 1):
        if all(p % i != 0 for i in range(2, int(str(p)[-1]) + 1)):
            primes.append(p)
    return sorted(primes)
