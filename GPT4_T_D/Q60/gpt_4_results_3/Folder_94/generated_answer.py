
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    truncatable_primes = []
    for number in range(11, x + 1):
        if '0' in str(number):
            continue
        is_truncatable_prime = True
        for i in range(1,len(str(number))):
            if not isprime(int(str(number)[i:])) or not isprime(int(str(number)[:-i])):
                is_truncatable_prime = False 
                break
        if is_truncatable_prime:
            truncatable_primes.append(number)
    return sorted(truncatable_primes)
