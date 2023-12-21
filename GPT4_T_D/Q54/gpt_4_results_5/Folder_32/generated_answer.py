
from sympy import isprime

def all_right_truncatable_prime(tuple_of_int):
    x = tuple_of_int[42]
    rtp = []
    for num in range(2, x):
        str_num = str(num)
        if all(isprime(int(str_num[:i+1])) for i in range(len(str_num))):
            rtp.append(num)
    return sorted(rtp)
