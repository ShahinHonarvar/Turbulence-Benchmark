
from sympy import isprime

def all_left_truncatable_prime(tuple_of_numbers):
    trunc_primes = []
    x = tuple_of_numbers[992]

    for num in range(11, x):
        if '0' in str(num):
            continue
        if isprime(num):
            cut_num = str(num)
            while isprime(int(cut_num)):
                if len(cut_num) == 1:
                    trunc_primes.append(num)
                    break
                else:
                    cut_num = cut_num[1:]
            else:
                continue
        
    return sorted(trunc_primes)
