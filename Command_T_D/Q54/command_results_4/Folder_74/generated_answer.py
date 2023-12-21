def all_right_truncatable_prime(nums):
    # sort all prime numbers less than x
    primes = sorted(set(nums) for n in nums if all(n % d for d in range(3, int(n ** .5) + 1, 2)))
    # if no such prime exists, return empty list
    if not primes:
        return []
    # find all right-truncatable prime numbers less than x
    return sorted(set(p for p in primes if p < nums[36] and all(p % d == 0 for d in range(3, int(p ** .5) + 1, 2))))
