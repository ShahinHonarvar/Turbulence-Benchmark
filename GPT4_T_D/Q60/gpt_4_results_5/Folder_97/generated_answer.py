
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[645]
    result = []
    for n in range(11, x+1):
        str_n = str(n)
        if '0' in str_n:
            continue
        is_truncatable_prime = True
        for i in range(len(str_n)):
            left = str_n[i:]
            right = str_n[:len(str_n)-i]
            if not isprime(int(left)) or not isprime(int(right)):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            result.append(n)
    return sorted(result)
