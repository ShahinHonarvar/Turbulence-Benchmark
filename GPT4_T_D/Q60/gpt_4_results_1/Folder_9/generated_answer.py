
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = []
    for number in range(2, x + 1):
        if isprime(number) and '0' not in str(number):
            temp = str(number)
            while len(temp) > 1:
                temp = temp[1:-1]
                if not isprime(int(temp)):
                    break
            else:
                primes.append(number)
    return sorted(primes, reverse=True)
