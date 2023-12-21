
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[466]
    primes = []
    for number in range(2, x):
        str_num = str(number)
        while str_num:
            if isprime(int(str_num)):
                str_num = str_num[:-1]
            else:
                break
        else:
            primes.append(number)
    return sorted(primes, reverse = True)
