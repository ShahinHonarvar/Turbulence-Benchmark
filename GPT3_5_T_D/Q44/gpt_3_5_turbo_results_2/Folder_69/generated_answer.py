
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(29, 80):
        if any(i % j == 0 for j in range(2, int(i**0.5) + 1)):
            composites.add(nums[i])
    return composites
