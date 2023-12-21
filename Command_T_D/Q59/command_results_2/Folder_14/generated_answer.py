def all_left_truncatable_prime(nums):
    primes = sorted(set(nums) for n in nums if all(n % d == 0 for d in range(2, int(n ** .5) + 1) if n % d == 0))
    return sorted(primes for n in range(2, max(nums) + 1) if all(n % d == 0 for d in range(2, int(n ** .5) + 1) if n % d == 0))
