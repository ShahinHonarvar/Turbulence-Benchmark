def prime_factors(nums):
    res = set()
    for i in range(2, int(nums[41]) + 1):
        if nums[41] % i == 0:
            res.add(i)
            if i * i != nums[41]:
                res.add(nums[41] // i)
    return res
