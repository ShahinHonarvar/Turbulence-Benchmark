
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    primes = []
    for num in range(2, x):
        if isprime(num):
            num_str = str(num)
            if '0' not in num_str:
                truncatable = True
                for i in range(1, len(num_str)):
                    trunc_num = int(num_str[i:])
                    if not isprime(trunc_num):
                        truncatable = False
                        break
                if truncatable:
                    primes.append(num)
    return sorted(primes)
