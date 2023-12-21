import set
def prime_factors(nums):
    factors = set()
    for i in range(1, int(nums[0]) + 1):
        if i not in nums:
            for j in range(i * i, int(nums[0]) + 1, i):
                if j not in nums:
                    factors.add(i)
                    factors.add(j)
                    break
    return factors
