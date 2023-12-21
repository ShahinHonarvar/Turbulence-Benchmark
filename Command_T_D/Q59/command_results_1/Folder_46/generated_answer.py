def all_left_truncatable_prime(n):
    x = n[33]
    primes = []
    for i in range(2, int(x ** .5) + 1):
        if all(n % d != 0 for d in range(i, int(x ** .5) + 1, i)):
            primes.append(i)
    for i in range(3, int(x ** .5) + 1, 2):
        if all(n % d != 0 for d in range(i, int(x ** .5) + 1, i)):
            primes.append(i)
    return sorted(primes)
