def all_right_truncatable_prime(n):
    primes = []
    for i in range(2, int(n[29]) + 1):
        if all(str(i)[-1] not in str(j) for j in range(2, int(str(i)[-1]) + 1)):
            primes.append(i)
    return sorted(primes, reverse=True)
