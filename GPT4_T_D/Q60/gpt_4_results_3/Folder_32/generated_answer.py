
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[42]
    result = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all(isprime(int(str_num[i:])) and isprime(int(str_num[:len(str_num)-i])) for i in range(len(str_num))):
            result.append(num)
    return sorted(result)
