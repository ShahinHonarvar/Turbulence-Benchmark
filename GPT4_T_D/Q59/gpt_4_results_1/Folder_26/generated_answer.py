
from itertools import permutations
from sympy import isprime


def all_left_truncatable_prime(int_tuple):
    def is_left_truncatable(num):
        if '0' in str(num):
            return False
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    x = int_tuple[81]
    possible_primes = [''.join(p) for i in range(1, len(str(x))) for p in permutations('123456789', i)]
    left_truncatable_primes = [int (item) for item in possible_primes if is_left_truncatable(int(item)) and int(item) < x ]
    left_truncatable_primes.sort(reverse=True)
    
    return left_truncatable_primes
