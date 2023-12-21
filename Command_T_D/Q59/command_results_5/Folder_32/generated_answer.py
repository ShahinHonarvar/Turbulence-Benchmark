def all_left_truncatable_prime(n):
    x = n[42]
    primes = []
    for i in range(2, int(x**(0.5)) + 1):
        while i**2 <= x:
            i += 1
        if all(i % d for d in range(2, int(x**(0.5)) + 1)):
            primes.append(i)
    return sorted(primes)
