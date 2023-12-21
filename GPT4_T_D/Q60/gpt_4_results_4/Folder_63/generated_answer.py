
import itertools

def all_left_right_truncatable_prime(nums):
    x = nums[88]
    prime_nums = [i for i in range(2, x + 1) if all(i % p > 0 for p in range(2, int(i ** .5) + 1))]
    right_truncatable_primes = [p for p in prime_nums if all(int(str(p)[:-i]) in prime_nums for i in range(1, len(str(p))))]
    left_right_truncatable_primes = [p for p in right_truncatable_primes if all(int(str(p)[i:]) in prime_nums for i in range(1, len(str(p))))]
    no_zero_primes = [p for p in left_right_truncatable_primes if '0' not in str(p)]
    return sorted(no_zero_primes)
