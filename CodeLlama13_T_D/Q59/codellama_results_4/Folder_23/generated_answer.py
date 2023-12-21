
def all_left_truncatable_prime(x):
    primes = []
    for i in range(10**7, x):
        if is_prime(i) and not contains_zero(i):
            primes.append(i)
    
    return sorted(primes, reverse=True)
