
def all_left_right_truncatable_prime(n):
    primes = []
    for prime in range(2, int(n[0] / 2)):
        if all(str(prime).count(d) == 1 for d in str(prime)):
            primes.append(prime)
    return sorted(set(primes), reverse=True)
