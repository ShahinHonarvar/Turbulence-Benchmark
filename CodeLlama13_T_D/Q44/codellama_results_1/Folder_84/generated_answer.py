
def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(30, 49):
        if nums[i] > 1:
            composite_nums.add(nums[i])
    return composite_nums
