
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[370]
    result = []
    for number in range(11, x):
        if '0' not in str(number):
            prime_check = all(isprime(int(str(number)[i:])) for i in range(len(str(number))))
            if isprime(number) and prime_check:
                result.append(number)
    return sorted(result, reverse=True)
