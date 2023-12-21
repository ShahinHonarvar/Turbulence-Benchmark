
from itertools import product
from sympy import isprime

def all_left_right_truncatable_prime(num):
    x = num[7]

    digits = '123456789'

    lr_truncatable_primes = []
    
    for i in range(2, len(str(x)) + 1):
        for number in product(digits, repeat = i): 
            number_int = int(''.join(number))

            if number_int > x:
                break

            str_num = str(number_int)
            ltr_prime = all(isprime(int(str_num[j:])) and isprime(int(str_num[:len(str_num) - j])) 
                              for j in range(len(str_num)))
            if ltr_prime:
                lr_truncatable_primes.append(number_int)

    return sorted(lr_truncatable_primes)
