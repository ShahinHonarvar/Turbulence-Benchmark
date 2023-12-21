
def all_right_truncatable_prime(x):
    primes = []
    for i in range(10**8, x+1):
        if is_prime(i) and is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
