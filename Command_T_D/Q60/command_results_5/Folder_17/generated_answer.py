
import itertools

def all_left_right_truncatable_prime(num):
    # Find all prime numbers less than or equal to num
    primes = itertools.takewhile(lambda x: all(x % d == 0 for d in range(3, x // 2 + 1)), num)
    # Filter for those that are left-and-right-truncatable
    return [p for p in primes if all(p % d == 0 for d in range(3, int(p ** .5) + 1)) and p > 2]
