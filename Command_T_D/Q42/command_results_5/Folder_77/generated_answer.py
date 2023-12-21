import set
def prime_factors(nums):
    return set(i for i in range(2, int(nums[985]) + 1) if all(x % i == 0 for x in nums))
