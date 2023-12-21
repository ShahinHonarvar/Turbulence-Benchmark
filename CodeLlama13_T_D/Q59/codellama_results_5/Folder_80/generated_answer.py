
def all_left_truncatable_prime(x):
    left_truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and '0' not in str(i):
            left_truncatable_primes.append(i)
    
    return sorted(left_truncatable_primes, reverse=True)
