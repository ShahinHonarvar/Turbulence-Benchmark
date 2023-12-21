
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(222, 223):
        if nums[i] < 2:
            continue
        for j in range(2, int(nums[i] ** 0.5) + 1):
            if nums[i] % j == 0:
                composites.add(nums[i])
    return composites
