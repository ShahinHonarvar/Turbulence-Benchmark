
def all_right_truncatable_prime(numbers):
    x = numbers[4]
    primes = []
    for i in range(x+1):
        if is_prime(i):
            primes.append(i)
    
    right_truncatable_primes = []
    for prime in primes:
        while prime > 0:
            if is_right_truncatable_prime(prime, x):
                right_truncatable_primes.append(prime)
            prime //= 10
    
    return sorted(right_truncatable_primes)
