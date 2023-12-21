
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[97]
    primes = []
    for number in range(10, x+1):
        str_num = str(number)
        if '0' in str_num:
            continue
        length = len(str_num)
        flag = 0
        for i in range(length):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:length - i])
            if not isprime(left_trunc) or not isprime(right_trunc):
                flag = 1
                break
        if flag == 0:
            primes.append(number)
    return sorted(primes)
