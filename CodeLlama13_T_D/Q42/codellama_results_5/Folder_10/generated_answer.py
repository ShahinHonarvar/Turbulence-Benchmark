
def prime_factors(nums):
    return set(reduce(operator.mul, (prime_factor(n) for n in nums[54:60]), 1))
