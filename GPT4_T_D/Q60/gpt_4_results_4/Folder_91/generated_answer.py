
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[0]
    lr_primes = []
    for number in range(10, x+1):
        if '0' not in str(number) and isprime(number):
            is_lr_prime = True
            for i in range(1, len(str(number))):
                if not isprime(int(str(number)[i:])) or not isprime(int(str(number)[:i])):
                    is_lr_prime = False
                    break
            if is_lr_prime:
                lr_primes.append(number)
    return sorted(lr_primes, reverse=True)
