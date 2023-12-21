def all_right_truncatable_prime(n):
    primes = [(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)]
    x = n[38]
    for p in primes:
        if p > x:
            break
        if x % p == 0:
            continue
        for d in range(10):
            q = int(str(x)[-1])
            if q > d:
                break
            x = int(str(x)[0:-1])
    return [] if x <= 3 else [p for p in primes if p < x]
