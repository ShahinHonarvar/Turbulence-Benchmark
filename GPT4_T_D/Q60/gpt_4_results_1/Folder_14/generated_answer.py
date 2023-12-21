
from sympy import isprime

def all_left_right_truncatable_prime(p_tuple):
    
    def truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):  
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s)-i])):
                return False
        return True

    x = p_tuple[78]
    truncatable_primes = [i for i in range(10, x + 1) if truncatable(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
