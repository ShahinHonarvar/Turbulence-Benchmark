import math
def all_left_truncatable_prime(n):
    primes = []
    for p in range(3, int(math.ceil(math.sqrt(n)) + 1)):
        if all(int(d) for d in str(p)):
            primes.append(p)
    return sorted(primes, reverse=True)
