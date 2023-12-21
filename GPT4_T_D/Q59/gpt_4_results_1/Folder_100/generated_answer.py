
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[26]
    
    def check_left_truncatable(prime):
        prime_str = str(prime)
        if "0" in prime_str:
            return False
        for i in range(len(prime_str)):
            if not isprime(int(prime_str[i:])):
                return False
        return True

    left_truncatable_primes = [i for i in range(2, x) if isprime(i) and check_left_truncatable(i)]
    return sorted(left_truncatable_primes)
