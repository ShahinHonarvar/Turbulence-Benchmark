def composite_nums_between_indices(nums):
    res = set()
    for i in range(1, 9):
        if i * i <= nums[7] and nums[i] != nums[0] and nums[i] != nums[8]:
            res.add(nums[i])
    return res
