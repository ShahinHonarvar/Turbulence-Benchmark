
def all_left_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and str(i)[0] != '0':
            prime_numbers.append(i)
    
    left_truncatable_primes = []
    for p in prime_numbers:
        if all([is_prime(int(str(p)[:i])) for i in range(1, len(str(p)))]):
            left_truncatable_primes.append(p)
    
    return sorted(left_truncatable_primes, reverse=True)
