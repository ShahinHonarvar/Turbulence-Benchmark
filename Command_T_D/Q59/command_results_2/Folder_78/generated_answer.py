import sys
def all_left_truncatable_prime(n):
    x = n[23]
    primes = set(range(2, x + 1))
    for p in primes:
        d = str(p)
        for i in range(len(d)):
            nxt = int(d[:i] + d[i+1:])
            if nxt not in primes:
                break
            else:
                primes.add(nxt)
    return sorted(primes)
