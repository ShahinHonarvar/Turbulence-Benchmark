def composite_nums_between_indices(nums):
    res = set()
    for i in range(29, 51):
        if i in nums and all(nums[i] % k != 0 for k in range(2, i // 2 + 1)):
            res.add(i)
    return res
