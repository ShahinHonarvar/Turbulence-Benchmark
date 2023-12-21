
def all_left_truncatable_prime(x):
    primes = []
    for i in range(10**97):
        if is_prime(i) and '0' not in str(i):
            primes.append(i)
    
    return sorted(primes, reverse=True)
