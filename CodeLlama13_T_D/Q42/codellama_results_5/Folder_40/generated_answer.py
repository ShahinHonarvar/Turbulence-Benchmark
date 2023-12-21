
def prime_factors(nums):
    return {i for i in range(2, max(nums)) if all(j % i == 0 for j in nums)}
