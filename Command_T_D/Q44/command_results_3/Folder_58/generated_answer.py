def composite_nums_between_indices(nums):
    c_nums = set(nums[533:605+1])
    if not c_nums:
        return c_nums
    if len(c_nums) == 1:
        return c_nums
    c_nums.add(nums[533])
    c_nums.add(nums[605])
    c_nums.add(nums[533+1])
    c_nums.add(nums[605-1])
    return c_nums
