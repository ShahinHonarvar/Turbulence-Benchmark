
from sympy import isprime

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[14]
    primes = []

    # Checks if the number is left-right truncatable
    def is_lr_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[i:])) and isprime(int(str_n[:len(str_n) - i])) for i in range(len(str_n)))

    for num in range(10, x+1):
        if '0' not in str(num) and is_lr_truncatable(num):
            primes.append(num)
            
    return sorted(primes)
