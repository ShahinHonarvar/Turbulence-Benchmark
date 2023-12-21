
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(22, 50+1):
        if nums[i-1] > 1:
            composites.add(nums[i-1])
    return composites
