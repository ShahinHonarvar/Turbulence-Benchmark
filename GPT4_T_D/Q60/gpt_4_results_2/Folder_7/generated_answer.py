
from sympy import isprime

def is_left_right_truncatable_prime(n):
    str_number = str(n)
    if '0' in str_number: 
        return False
    for i in range(len(str_number)):
        if not isprime(int(str_number[i:])) or not isprime(int(str_number[:len(str_number)-i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[803]
    return sorted([i for i in range(10, x+1) if is_left_right_truncatable_prime(i)])
