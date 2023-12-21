
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[22]
    result = []
    for number in range(2, x):
        str_num = str(number)
        if all(isprime(int(str_num[:i])) for i in range(len(str_num), 0, -1)):
            result.append(number)
    return sorted(result, reverse=True)
