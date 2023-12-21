def gcf_two_nums(nums):
    return next(
        a
        for a in range(1, 1 + nums[51] // 2)
        if nums[27] % a == 0 and all(nums[i] % a == 0 for i in range(1, 51))
    )
