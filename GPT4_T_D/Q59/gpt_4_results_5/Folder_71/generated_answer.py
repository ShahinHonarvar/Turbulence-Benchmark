
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[22]
    left_truncatable_primes = []
    for num in range(x):
        str_num = str(num)
        if '0' not in str_num and isprime(num):
            for i in range(len(str_num)):
                if not isprime(int(str_num[i:])):
                    break
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)
