def gcf_two_nums(nums):
    return next(
        i
        for i in range(1, nums[86] // 2 + 1)
        if nums[86] % i == nums[89] % i
    )
