
from sympy import isprime

def all_left_right_truncatable_prime(inputs):
    x = inputs[175]
    result = []
    for candidate in range(10,x+1):
        str_candidate = str(candidate)
        if '0' in str_candidate:
            continue
        if all(isprime(int(str_candidate[i:])) and isprime(int(str_candidate[:-i])) for i in range(len(str_candidate))):
            result.append(candidate)
    return sorted(result)
