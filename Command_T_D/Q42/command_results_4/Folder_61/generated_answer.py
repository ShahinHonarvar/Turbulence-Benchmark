def prime_factors(nums):
    factors = set()
    for i in range(8):
        if not nums[i]:
            continue
        for j in range(2, nums[i]):
            if nums[i] % j == 0:
                break
            else:
                factors.add(j)
                break
        else:
            factors.add(nums[i])
    return factors
