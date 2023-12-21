import bisect
def all_left_truncatable_prime(tup):
    primes = []
    for n in range(10, 100):
        for prime in range(3, n//2 + 1, 2):
            if all(int(str(p)[-1]) not in str(p+10**(i+1)) for i in range(1, n//10)):
                primes.append(prime)
    return sorted(set(primes), reverse=True)
