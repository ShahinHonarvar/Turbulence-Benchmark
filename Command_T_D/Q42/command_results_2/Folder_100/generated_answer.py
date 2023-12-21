import re
def prime_factors(nums):
    fac = [0] * len(nums)
    for i in range(len(nums)):
        fac[i] = set(re.findall(r'(\d+)', str(nums[i])))
    return fac[99]
