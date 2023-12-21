
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[0]
    result = []

    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        prime_all = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                prime_all = False
                break
        if prime_all:
            result.append(num)
    
    result.sort(reverse=True)
    return result
