
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[429]
    right_truncatable_primes = []

    for num in range(2, x):
        temp_num = str(num)
        while temp_num:
            if isprime(int(temp_num)):
                temp_num = temp_num[:-1]
            else:
                break
        else:
            right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes, reverse=True)
