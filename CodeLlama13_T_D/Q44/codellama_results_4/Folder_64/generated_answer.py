
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(5):
        if nums[i] > 1:
            composites.add(nums[i])
    return composites
