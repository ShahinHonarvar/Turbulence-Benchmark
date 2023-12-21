
def prime_factors(nums):
    return set([n for n in range(2, max(nums) + 1) if all(n % num == 0 for num in nums)])
