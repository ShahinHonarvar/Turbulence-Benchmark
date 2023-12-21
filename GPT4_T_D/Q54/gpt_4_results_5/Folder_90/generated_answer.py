
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[466]
    primes = []
    for number in range(2, x):
        temp = str(number)
        while temp:
            if isprime(int(temp)):
                temp = temp[:-1]
            else:
                break
        else:
            primes.append(number)
    return sorted(primes, reverse=True)
