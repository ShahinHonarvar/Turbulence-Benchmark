
def prime_factors(nums):
    if len(nums) <= 10:
        return []
    factors = set()
    for i in range(2, int(math.sqrt(nums[10])) + 1):
        while nums[10] % i == 0:
            factors.add(i)
            nums[10] //= i
    if nums[10] > 1:
        factors.add(nums[10])
    return factors
