
from sympy import isprime

def truncatable_left_and_right(num):
    num_str = str(num)
    if "0" in num_str:
        return False
    if len(num_str) == 1 or len(num_str) == 2:
        if isprime(int(num_str)):
            return True
        else:
            return False
    for i in range(len(num_str)):
        if not isprime(int(num_str[i:])):
            return False
        if not isprime(int(num_str[:len(num_str) - i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[39]
    result = []
    for i in range(2, x + 1):
        if truncatable_left_and_right(i):
            result.append(i)
    result.sort(reverse=True)
    return result
