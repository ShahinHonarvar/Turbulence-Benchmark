def all_right_truncatable_prime(n):
    x = n[85]
    primes = []
    for i in range(2, x // 2 + 1):
        j = str(i)
        while j[0] == '2':
            j = int(j[1:])
        if j in primes or all(p % j == 0 for p in primes):
            continue
        else:
            primes.append(j)
    return sorted(set(primes))
