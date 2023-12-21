
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[39]

    def left_right_truncation(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not (isprime(int(num_str[i:])) and isprime(int(num_str[:len(num_str)-i]))):
                return False
        return True

    truncatable_primes = [i for i in range(1, x+1) if ('0' not in str(i)) and left_right_truncation(i)]
    return sorted(truncatable_primes)
