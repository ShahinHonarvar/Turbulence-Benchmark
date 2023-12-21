
from sympy import isprime

def all_left_truncatable_prime(args):
    x = args[32]
    def is_left_truncatable_prime(num):
        if '0' in str(num): return False
        num_str = str(num)
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                return False
        return True

    primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)
