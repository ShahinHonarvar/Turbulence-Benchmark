
from sympy import isprime

def all_left_right_truncatable_prime(tup_of_nums):
    x = tup_of_nums[89]
    primes = [p for p in range(10, x + 1) if isprime(p) and '0' not in str(p)]
    truncatable_primes = []
    for p in primes:
        p_str = str(p)
        for i in range(len(p_str)):
            left_trun = p_str[i:]
            right_trun = p_str[:len(p_str)-i]
            if not isprime(int(left_trun)) or not isprime(int(right_trun)):
                break
        else:
            truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse = True)
