
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[6]
    result = []
    for number in range(11, x):
        str_num = str(number)
        if '0' in str_num:
            continue
        truncations = [int(str_num[i:]) for i in range(len(str_num))]
        if all(isprime(num) for num in truncations):
            result.append(number)
    return sorted(result, reverse=True)
