
import sympy

def all_right_truncatable_prime(numbers):
    x = numbers[975]
    right_truncatable_primes = []
  
    def is_right_truncatable_prime(number):
        while number > 0:
            if not sympy.isprime(number):
                return False
            number //= 10
        return True
  
    for num in range(x-1, 1, -1):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    
    return sorted(right_truncatable_primes, reverse=True)
