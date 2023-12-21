
import sympy

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    
    while len(str(n)) > 2:
        if not sympy.isprime(n):
            return False
        n = int(str(n)[1:-1])
    
    if len(str(n)) == 1:
        return sympy.isprime(n)
    else:
        return sympy.isprime(n) and sympy.isprime(int(str(n)[0]))

def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    truncatable_primes = []
    
    for n in range(2, x + 1):
        if is_left_right_truncatable_prime(n):
            truncatable_primes.append(n)
    
    return truncatable_primes
