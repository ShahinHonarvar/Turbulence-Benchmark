
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[33]
    truncatable_primes = []
    for number in range(2, x):
        if "0" not in str(number) and isprime(number):
            temp_num = str(number)
            while temp_num:
                if isprime(int(temp_num)):
                    temp_num = temp_num[1:]
                else:
                    break
            if not temp_num:
                truncatable_primes.append(number)
    return sorted(truncatable_primes)
