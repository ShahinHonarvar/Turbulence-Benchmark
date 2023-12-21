
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[91]
    truncatable_primes = []
    
    for num in range(2, x+1):
        str_num = str(num)
        if '0' in str_num:
            continue
        length = len(str_num)
        for i in range(length):
            if not isprime(int(str_num[i:])) or not isprime(int(str_num[:length - i])):
                break
        else:
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes)
