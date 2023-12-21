
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[175]
    prime_list = []
    for number in range(11, x):
        str_number = str(number)
        if '0' in str_number:
            continue
        truncatable = True
        for i in range(1, len(str_number)):
            if not isprime(int(str_number[i:])):
                truncatable = False
                break
        if truncatable and isprime(number):
            prime_list.append(number)
    return sorted(prime_list)
