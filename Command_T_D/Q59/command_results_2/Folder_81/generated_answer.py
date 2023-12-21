def all_left_truncatable_prime(x):
    primes = []
    for n in range(2, x):
        s = str(n)
        while s:
            if all(int(d) for d in s):
                primes.append(int(s))
                break
            s = s[1:]
    return sorted(primes)
