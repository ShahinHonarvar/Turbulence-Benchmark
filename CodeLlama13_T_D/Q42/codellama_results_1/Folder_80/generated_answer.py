
def prime_factors(nums):
    return {factor for num in nums[746] for factor in range(1, int(num ** 0.5) + 1) if num % factor == 0}
