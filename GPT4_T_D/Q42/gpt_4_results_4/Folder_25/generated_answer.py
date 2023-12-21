
def prime_factors(nums):
    num = nums[90]
    factors = set()
    for i in range(2, num+1):
        if num % i == 0:
            factors.add(i)
            while num % i == 0:
                num = num // i
    return factors
