
from sympy import isprime

def all_right_truncatable_prime(tpl):
    x = tpl[30]
    truncatable_primes = []
    for num in range(2, x):
        temp_num = str(num)
        while len(temp_num) > 0 and isprime(int(temp_num)):
            temp_num = temp_num[:-1]
        if len(temp_num) == 0:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)
