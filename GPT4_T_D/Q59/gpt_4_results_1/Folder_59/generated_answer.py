
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[84]
    left_truncatable_primes = []

    def is_left_truncatable(number):
        str_num = str(number)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return not '0' in str_num

    for i in range(1, x):
        if is_left_truncatable(i):
            left_truncatable_primes.append(i)

    return sorted(left_truncatable_primes, reverse=True)
