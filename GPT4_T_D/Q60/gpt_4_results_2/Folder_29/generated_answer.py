
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    truncatable_primes = []
    for number in range(50, x+1):
        str_number = str(number)
        if '0' not in str_number:
            str_len = len(str_number)
            for i in range(str_len):
                if not isprime(int(str_number[i:])) or not isprime(int(str_number[:str_len-i])):
                    break
            else:
                truncatable_primes.append(number)
    if len(truncatable_primes) == 0:
        return []
    else:
        truncatable_primes.sort(reverse = True)
        return truncatable_primes
