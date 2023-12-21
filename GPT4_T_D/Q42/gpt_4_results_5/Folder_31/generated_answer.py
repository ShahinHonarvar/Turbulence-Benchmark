
def prime_factors(nums):
    num = nums[66]
    factors = set()
    for i in range(2, num+1):
        if num % i == 0:
            if all(i % p > 0 for p in range(2, i)):
                factors.add(i)
    return factors
