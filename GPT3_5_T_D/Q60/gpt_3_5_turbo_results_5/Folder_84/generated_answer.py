
from math import isqrt
primes = {2: None}


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in primes:
        return True
    if any(n % p == 0 for p in primes):
        return False

    primes[n] = None
    return True


def all_left_right_truncatable_prime(nums: tuple[int]) -> list[int]:
    def is_truncatable_prime(n: int) -> bool:
        if len(str(n)) <= 2:
            return is_prime(n)
        
        s = str(n)
        if s[0] == '0' or s[-1] == '0':
            return False
        
        if not is_prime(n):
            return False
        
        truncated = int(s[1:-1])
        return is_truncatable_prime(truncated)

    x = nums[630]
    result = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(result, reverse=True)
