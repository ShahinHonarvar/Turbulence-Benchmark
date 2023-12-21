
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    if len(tup)<7: return []
    def truncate_check(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:len(str_n)-i])):
                return False
        return True
    x=tup[6]
    return sorted([i for i in range(10, x+1) if all(d !='0' for d in str(i)) and truncate_check(i) ],reverse=True)
