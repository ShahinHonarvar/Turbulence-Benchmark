
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            primes.append(i)
    
    truncatable_primes = []
    for prime in primes:
        if is_left_truncatable_prime(prime) and is_right_truncatable_prime(prime):
            truncatable_primes.append(prime)
    
    return sorted(truncatable_primes, reverse=True)
