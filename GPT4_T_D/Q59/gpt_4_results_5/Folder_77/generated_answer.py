
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[767]
    result = []
    for number in range(10, x):
        if '0' not in str(number) and isprime(number):
            for i in range(1, len(str(number))):
                if not isprime(int(str(number)[i:])):
                    break
            else:
                result.append(number)
    return sorted(result, reverse=True)
