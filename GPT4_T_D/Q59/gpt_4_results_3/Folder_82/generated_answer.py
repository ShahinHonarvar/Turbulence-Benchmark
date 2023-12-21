
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[69]
    range_list = range(10,x)
    primes = []
    for num in range_list:
        if '0' in str(num):
            continue
        num_str = str(num)
        is_truncatable = True
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(num)
    primes.sort(reverse=True)
    return primes
