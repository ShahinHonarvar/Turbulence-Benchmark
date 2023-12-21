
def all_left_truncatable_prime(numbers):
    x = numbers[126]
    primes = []
    for i in range(x):
        if is_prime(i) and not contains_zero(str(i)):
            primes.append(i)
    
    left_truncatable_primes = []
    for prime in primes:
        if is_left_truncatable_prime(prime):
            left_truncatable_primes.append(prime)
    
    return sorted(left_truncatable_primes, reverse=True)
