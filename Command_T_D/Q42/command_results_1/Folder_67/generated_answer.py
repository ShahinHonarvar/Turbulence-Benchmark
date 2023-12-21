def prime_factors(nums):
    fac = set()
    for i in range(2, int(nums[43]) + 1):
        if all(x % i != 0 for x in nums):
            fac.add(i)
            break
    return fac
