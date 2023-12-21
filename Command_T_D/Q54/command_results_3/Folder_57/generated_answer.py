import sys
def all_right_truncatable_prime(n):
    primes = []
    for x in range(2, int(n[1]) + 1):
        if x == 2 or x == 3:
            continue
        if all(str(x) % 10 not in str(x**i) for i in range(1, int(x**0.5) + 1)):
            primes += [x]
    return primes
