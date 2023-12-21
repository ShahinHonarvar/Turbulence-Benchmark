
from sympy import isprime

def all_left_truncatable_prime(tuple_input):
    x = tuple_input[945]

    def is_left_truncatable_prime(num):
        if "0" in str(num):
            return False
        while num != 0:
            if not isprime(num):
                return False
            num = int(str(num)[1:]) if len(str(num)) > 1 else 0
        return True

    left_truncatable_primes = [i for i in range(11, x) if is_left_truncatable_prime(i)]
    return sorted(left_truncatable_primes, reverse=True)
