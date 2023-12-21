
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[975]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if all(isprime(int(str_num[:i])) for i in range(1, len(str_num) + 1)):
            primes.append(num)
    return sorted(primes, reverse = True)
