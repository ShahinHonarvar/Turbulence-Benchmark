
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[57]
    primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        flag = True
        str_num = str(num)
        for i in range(len(str_num)):
            if not(isprime(int(str_num[i:])) and isprime(int(str_num[:len(str_num)-i]))):
                flag = False
                break
        if flag:
            primes.append(num)
    return sorted(primes, reverse=True)
