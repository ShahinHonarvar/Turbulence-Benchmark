
def all_right_truncatable_prime(numbers):
    x = numbers[85]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    
    truncatable_primes = []
    for prime in prime_numbers:
        str_prime = str(prime)
        while len(str_prime) > 1:
            last_digit = int(str_prime[-1])
            str_prime = str_prime[:-1]
            if not is_prime(int(str_prime)):
                break
        
        if len(str_prime) == 1:
            truncatable_primes.append(prime)
    
    return sorted(truncatable_primes)
