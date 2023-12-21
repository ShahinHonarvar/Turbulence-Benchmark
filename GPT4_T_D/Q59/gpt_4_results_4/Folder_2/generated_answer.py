
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[618]

    def is_left_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])):
                return False
        return True

    lt_primes = [i for i in range(10, x) if is_left_truncatable_prime(i)]
      
    return sorted(lt_primes)
