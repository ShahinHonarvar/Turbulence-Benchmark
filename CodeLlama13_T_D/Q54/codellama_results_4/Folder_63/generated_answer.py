
def all_right_truncatable_prime(numbers):
    x = numbers[88]
    prime_numbers = []
    
    for i in range(2, x):
        if is_prime(i):
            prime_numbers.append(i)
            
    right_truncatable_primes = []
    
    for p in prime_numbers:
        if is_right_truncatable_prime(p):
            right_truncatable_primes.append(p)
            
    return sorted(right_truncatable_primes)

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while len(str(n)) > 1:
        if not is_prime(n):
            return False
        n //= 10
    return True
