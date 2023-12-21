def all_left_truncatable_prime(n):
    x = int(n[78])
    primes = []
    for i in range(2, x // 2):
        if all(str(i).count(d) == 1 for d in str(i)):
            primes.append(i)
    for i in range(2, x // 2):
        if all(str(i).count(d) == 1 for d in str(i)):
            primes.append(i)
    return sorted(set(primes))
