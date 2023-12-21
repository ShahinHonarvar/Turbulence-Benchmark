
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[35]
    left_primes = []

    for num in range(10, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        num_list = [int(str_num[i:]) for i in range(len(str_num))]
        if all(isprime(n) for n in num_list):
            left_primes.append(num)

    return sorted(left_primes, reverse=True)
