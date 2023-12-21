
from sympy import isprime

def all_left_truncatable_prime(t):
    def is_left_truncatable(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        while len(num_str)>0:
            if not isprime(int(num_str)):
                return False
            num_str = num_str[1:]
        return True

    x = t[758]
    lt_primes = [n for n in range(11, x) if is_left_truncatable(n)]
    return sorted(lt_primes)
