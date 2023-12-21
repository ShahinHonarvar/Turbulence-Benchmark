
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[78]
    right_truncatable_primes = []
    for number in range(2, x):
        str_num = str(number)
        right_truncate = [str_num[:-i] for i in range(len(str_num))]
        if all(isprime(int(n)) for n in right_truncate):
            right_truncatable_primes.append(number)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
