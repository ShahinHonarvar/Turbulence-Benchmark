
from itertools import permutations

def all_left_right_truncatable_prime(int_tuple):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        length = len(str(n))
        for i in range(length):
            left_trunc = int(str(n)[i:])
            right_trunc = int(str(n)[:length-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    
    x = int_tuple[41]
    primes = [str(i) for i in range(10, x+1) if is_prime(i)]
    truncatable_primes = sorted([int(''.join(p)) for p in permutations(primes) if is_truncatable_prime(int(''.join(p)))])

    return truncatable_primes[::-1]
