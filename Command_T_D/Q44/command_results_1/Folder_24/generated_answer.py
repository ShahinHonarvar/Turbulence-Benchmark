import set
def composite_nums_between_indices(nums):
    c_set = set()
    for i in range(34, 55):
        if nums[i] % 2 == 0 and nums[i] != 1:
            c_set.add(nums[i])
    return c_set
