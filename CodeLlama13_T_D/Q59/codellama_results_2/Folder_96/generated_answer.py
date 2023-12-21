
def all_left_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not '0' in str(i):
            primes.append(i)
    return sorted([i for i in primes])
