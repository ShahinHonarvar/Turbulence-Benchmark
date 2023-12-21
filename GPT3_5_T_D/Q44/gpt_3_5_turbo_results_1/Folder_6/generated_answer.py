
def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(13, 69):
        if all(nums[i] % j != 0 for j in range(2, int(nums[i] ** 0.5) + 1)):
            continue
        composite_nums.add(nums[i])
    return composite_nums
