
def prime_factors(nums):
    number = nums[66]
    factors = set()
    for i in range(2, number + 1):
        while number % i == 0:
            factors.add(i)
            number = number // i
    return factors
