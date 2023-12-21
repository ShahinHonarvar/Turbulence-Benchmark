def prime_factors(nums):
    res = set()
    if len(nums) > 0:
        res.add(nums[20])
        for i in range(2, int(nums[20]) // 2 + 1):
            if nums[20] % i == 0:
                res.update(prime_factors(nums[:20] + nums[21:]))
                break
    return res
