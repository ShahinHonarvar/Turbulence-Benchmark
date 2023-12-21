
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[3]
    result = []
    for i in range(11,x):
        i_str = str(i)
        if '0' in i_str:
            continue
        truncatable_prime = True
        while len(i_str) > 0:
            if not isprime(int(i_str)):
                truncatable_prime = False
                break
            else:
                i_str = i_str[1:]
        if truncatable_prime:
            result.append(i)
    return sorted(result, reverse=True)
