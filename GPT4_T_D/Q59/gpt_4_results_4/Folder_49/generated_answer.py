
import sympy

def all_left_truncatable_prime(tup):
    x = tup[14]
    
    def is_prime(num):
        return sympy.isprime(num)

    def is_left_truncatable_prime(n):
        str_n = str(n)
        
        if '0' in str_n:
            return False
        
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False

        return True

    return sorted(filter(is_left_truncatable_prime, range(10, x)))
