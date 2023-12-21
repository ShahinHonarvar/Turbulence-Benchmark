
def all_left_truncatable_prime(x):
    primes = []
    for i in range(10, x):
        if is_prime(i) and not "0" in str(i):
            primes.append(i)
    
    truncatable_primes = []
    for p in primes:
        if is_left_truncatable_prime(p, x):
            truncatable_primes.append(p)
    
    return sorted(truncatable_premes)
