
def prime_factors(nums):
    return set([p for n in nums[95] for p in range(2, int(n**0.5) + 1) if n % p == 0])
