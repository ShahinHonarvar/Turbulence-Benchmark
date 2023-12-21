
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(20, 201):
        if nums[i] > 1 and nums[i] % nums[i-1] == 0:
            composites.add(nums[i])
    return composites
