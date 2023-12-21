
from sympy import isprime

def all_left_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[175]
    truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            len_str = len(str_num)
            all_are_primes = True
            for i in range(len_str):
                if not isprime(int(str_num[i:])) or not isprime(int(str_num[:len_str - i])):
                    all_are_primes = False
                    break
            if all_are_primes:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)
