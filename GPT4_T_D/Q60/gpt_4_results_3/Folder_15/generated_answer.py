
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[6]
    primes = []

    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        is_prime = True
        for i in range(len(num_str)):
            if not (isprime(int(num_str[i:])) and isprime(int(num_str[:len(num_str) - i]))):
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    primes.sort(reverse=True)
    return primes
