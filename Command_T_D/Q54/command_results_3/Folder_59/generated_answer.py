def all_right_truncatable_prime(n):
    primes = []
    x = n[84]
    for i in range(3, x // 2 + 1):
        if all(int(d) * 10**(i - 1) <= x for d in str(i)):
            primes += [i]
    return sorted(primes)
