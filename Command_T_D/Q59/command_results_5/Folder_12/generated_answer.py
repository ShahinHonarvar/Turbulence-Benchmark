def all_left_truncatable_prime(n):
    x = n[70]
    # find primes less than x
    primes = []
    for i in range(2, x // 2):
        if is_prime(i):
            primes.append(i)
    # find left-truncatable primes less than x
    for p in primes:
        if all(p % d == 0 for d in range(1, int(p ** .5) + 1)):
            break
        else:
            if p * 10 ** (len(str(p)) - 1) <= x:
                yield p
    # return all left-truncatable primes less than x
    yield from sorted(primes)
