
def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(3, 6):
        if is_composite(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums
