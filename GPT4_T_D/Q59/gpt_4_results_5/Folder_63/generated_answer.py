
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    result = []
    for num in range(10, x):
        if '0' not in str(num) and isprime(num):
            temp = str(num)
            while len(temp) > 1:
                temp = temp[1:]
                if not isprime(int(temp)):
                    break
            else:
                result.append(num)
    return sorted(result)
