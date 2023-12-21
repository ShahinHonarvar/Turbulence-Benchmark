
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[67]
    primes = []
    for number in range(10, x):
        str_number = str(number)
        if '0' in str_number:
            continue
        prime_flag = all(isprime(int(str_number[i:])) for i in range(len(str_number)))
        if prime_flag:
            primes.append(number)
    primes.sort(reverse=True)
    return primes
