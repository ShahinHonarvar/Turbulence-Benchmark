def composite_nums_between_indices(nums):
    res = set()
    for i in range(14, 65):
        if not nums[i]:
            continue
        res.update(nums[i])
    return res
