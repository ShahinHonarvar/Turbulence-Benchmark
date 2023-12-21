def all_left_truncatable_prime(n):
    primes = []
    for i in range(3, n[0] // 2 + 1):
        if all(int(d) for d in str(i)):
            if i % 2 == 1 and all(p % i == 0 for p in range(3, int(str(i)) + 1, i)):
                primes.append(i)
            elif i % 2 == 0 and all(p % i == 0 for p in range(5, int(str(i)) + 1, i)):
                primes.append(i)
    return sorted(primes)
