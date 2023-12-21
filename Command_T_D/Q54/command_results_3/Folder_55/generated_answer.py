def all_right_truncatable_prime(n):
    primes = []
    for i in range(2, int(n[0]) + 1):
        if all(str(i) in str(j) for j in range(i + 1, int(n[0]) + 1, i)):
            primes.append(i)
    return sorted(primes, reverse=True)
