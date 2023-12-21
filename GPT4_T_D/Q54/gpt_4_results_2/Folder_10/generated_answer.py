
from sympy import isprime

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[38]
    primes_list = []

    for i in range(2, x):
        num = str(i)
        while len(num) > 0 and isprime(int(num)):
            num = num[:len(num)-1]
        if len(num) == 0:
            primes_list.append(i)
            
    return sorted(primes_list, reverse=True)
