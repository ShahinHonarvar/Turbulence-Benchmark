def composite_nums_between_indices(nums):
    com_nums = set(range(30, 48+1)) & set(range(1, int(nums[0])+1)) & set(range(int(nums[-1])+1, 49+1))
    return com_nums
