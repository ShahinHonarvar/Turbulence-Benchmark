
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[98]
    right_truncatable_primes = []
    for i in range(2, x):
        status = True
        number_string = str(i)
        j = len(number_string)
        while j > 0:
            if not isprime(int(number_string[:j])):
                status = False
                break
            j -= 1
        if status:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
