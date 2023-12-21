
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[24]
    return_list = []
    for i in range(13, x):
        if contain_zero(i):
            continue
        if is_left_truncatable_prime(i):
            return_list.append(i)
    return sorted(return_list)

def contain_zero(n):
    while n > 0:
        if n % 10 == 0:
            return True
        n = n // 10
    return False

def is_left_truncatable_prime(number):
    str_num = str(number)
    for i in range(len(str_num)):
        if not isprime(int(str_num[i:])):
            return False
    return True
