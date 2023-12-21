
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def check(num):
        num = str(num)
        if '0' in num: return False
        for i in range (len(num)):
            if not isprime(int(num[i:])) or not isprime(int(num[:len(num)-i])):
                return False
        return True
    
    x = tup[70]
    trucatable_primes = [i for i in range(11, x+1) if check(i)]
    return sorted(trucatable_primes, reverse=True)
