
from sympy import isprime

def left_truncatable_prime(n):
    if '0' in str(n):
        return False
    if n < 10:
        return isprime(n)
    elif isprime(n) and left_truncatable_prime(int(str(n)[1:])):
        return True
    else:
        return False
        
def all_left_truncatable_prime(t): 
    x = t[41]
    result = []
    for i in range(11, x):  
        if left_truncatable_prime(i):
            result.append(i)
    return sorted(result)
