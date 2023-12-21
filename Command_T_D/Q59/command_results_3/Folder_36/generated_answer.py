def all_left_truncatable_prime(nums):
    primes = [n for n in range(2, int(str(nums[0]))) if all(str(n) not in str(x) for x in range(2, int(str(n)) + 1) if x % 10 != 0)]
    return primes
