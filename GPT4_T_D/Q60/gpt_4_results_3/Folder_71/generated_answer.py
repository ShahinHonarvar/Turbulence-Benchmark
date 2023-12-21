
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def check_truncatable(prime):
        str_prime = str(prime)
        if '0' in str_prime:
            return False
        for i in range(len(str_prime)):
            if not isprime(int(str_prime[i:])) or not isprime(int(str_prime[:len(str_prime)-i])):
                return False
        return True

    x = tup[22]
    return sorted([i for i in range(11, x) if isprime(i) and check_truncatable(i)], reverse=True)
