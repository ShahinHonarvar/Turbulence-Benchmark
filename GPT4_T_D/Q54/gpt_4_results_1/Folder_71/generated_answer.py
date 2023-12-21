
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[22]
    rt_primes = []
    for number in range(x-1, 1, -1):
        if isprime(number):
            str_num = str(number)
            while len(str_num) > 1:
                str_num = str_num[:-1]
                if not isprime(int(str_num)):
                    break
            else:
                rt_primes.append(number)
    return sorted(rt_primes, reverse=True)
