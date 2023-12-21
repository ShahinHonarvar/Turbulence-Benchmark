
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not str(i).startswith('0'):
            primes.append(i)
    
    left_right_truncatable_primes = []
    for prime in primes:
        if is_left_and_right_truncatable_prime(prime):
            left_right_truncatable_primes.append(prime)
    
    return sorted(left_right_truncatable_primes, reverse=True)
