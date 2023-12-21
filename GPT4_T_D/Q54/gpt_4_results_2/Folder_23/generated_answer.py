
from sympy import isprime

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 77:
        return []
    x = numbers[77]
    right_truncatable_primes = []
    for i in range(2, x):
        if isprime(i):
            str_i = str(i)
            is_right_truncatable = True
            while len(str_i) > 1:
                str_i = str_i[:-1]
                if not isprime(int(str_i)):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
