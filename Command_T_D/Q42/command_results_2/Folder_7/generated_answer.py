def prime_factors(nums):
    res = set()
    for i in range(2, int(nums[851]) + 1):
        if all(nums[idx] % i != 0 for idx in range(851)):
            res.add(i)
            break
    return res
