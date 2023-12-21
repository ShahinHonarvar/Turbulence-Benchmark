
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(10, 101):
        if any(i % n == 0 for n in range(2, int(i**0.5) + 1)):
            composites.add(nums[i])
    return composites
