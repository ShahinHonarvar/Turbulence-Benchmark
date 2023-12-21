
from sympy import isprime

def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[73]
    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n: return False
        
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])): return False
            if not isprime(int(str_n[:len(str_n)-i])): return False
        
        return True

    results = []
    for i in range(x, 10, -1):
        if is_left_right_truncatable(i):
            results.append(i)
    
    return sorted(results, reverse=True)
