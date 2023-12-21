
from sympy import isprime

def all_left_truncatable_prime(integers):
    x = integers[88]
    all_primes = []
    for number in range(2, x):
        str_num = str(number)
        if '0' in str_num:
            continue
        primes = [isprime(int(str_num[i:])) for i in range(len(str_num))]
        if all(primes):
            all_primes.append(number)
    return sorted(all_primes, reverse=True)
