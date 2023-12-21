
from sympy import isprime

def all_left_right_truncatable_prime(lst):
    x = lst[55]
    truncatable_primes = []
    for number in range(10, x + 1):
        if '0' in str(number): 
            continue
        str_num = str(number)
        for i in range(len(str_num)):
            left_truncatable = isprime(int(str_num[i:]))  
            right_truncatable = isprime(int(str_num[:len(str_num) - i])) 
            if not left_truncatable or not right_truncatable:
                break
        else:
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)
