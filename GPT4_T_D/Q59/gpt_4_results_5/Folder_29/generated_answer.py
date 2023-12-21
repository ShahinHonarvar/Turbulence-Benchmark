
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[55]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' not in str_num:
            primes_list = [int(str_num[i:]) for i in range(len(str_num))]
            if all(isprime(p) for p in primes_list):
                primes.append(num)
    return sorted(primes, reverse=True)
