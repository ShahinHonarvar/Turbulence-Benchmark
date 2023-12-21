def all_left_truncatable_prime(n):
    x = n[70]
    primes = set(range(2, int(str(x)[0])))
    while len(primes) > 0:
        prime = primes.pop()
        if str(prime)[0] == str(prime)[1]:
            continue
        nxt = str(prime)[0]
        while nxt:
            nxt = int(str(prime)[0])
            if nxt in primes:
                break
            primes.add(nxt)
    return sorted(primes)
