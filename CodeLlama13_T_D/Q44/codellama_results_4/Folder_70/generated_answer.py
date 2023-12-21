
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(32, 36):
        if nums[i] > 1:
            composites.add(nums[i])
    return composites
