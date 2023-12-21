
def all_left_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
