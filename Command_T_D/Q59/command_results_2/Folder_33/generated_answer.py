import re
import bisect
def all_left_truncatable_prime(n):
    is_left_truncatable_prime = lambda i: not i.lstrip('0') and re.fullmatch(r'[2-9]0*', i)
    left_truncatable_primes = []
    for num in range(3, int(str(n[0])[0]) + 1):
        if is_left_truncatable_prime(str(num)):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
