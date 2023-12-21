
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[433]
    primes = []
    for number in range(x):
        if '0' not in str(number) and isprime(number):
            temp = str(number)
            while temp != '':
                if isprime(int(temp)):
                    temp = temp[1:]
                else:
                    break
            else:
                primes.append(number)
    return sorted(primes, reverse=True)
