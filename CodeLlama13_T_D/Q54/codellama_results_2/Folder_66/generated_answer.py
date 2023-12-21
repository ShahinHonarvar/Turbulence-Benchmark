
def all_right_truncatable_prime(numbers):
    x = numbers[25]
    prime_numbers = []
    for i in range(10, x + 1):
        if is_prime(i):
            prime_numbers.append(i)
    
    right_truncatable_primes = []
    for i in prime_numbers:
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    
    return sorted(right_truncatable_primes, reverse=True)
