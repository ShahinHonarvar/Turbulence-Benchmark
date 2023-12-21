import set
def prime_factors(nums):
    return set(prime_factors(num for num in range(2, int(nums[459]) + 1) if all(num % r == 0 for r in range(2, int(num ** .5) + 1)))
