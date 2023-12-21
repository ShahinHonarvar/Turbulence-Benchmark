def all_left_truncatable_prime(n):
    primes = []
    for n in range(2, int(str(n[0])[0]) + 1):
        if all(str(n).count(d) == 1 for d in str(n)):
            primes += [n]
            for d in str(n):
                n = int(d)
                if all(str(n).count(d) == 1 for d in str(n)):
                    primes += [n]
    return sorted(primes)
