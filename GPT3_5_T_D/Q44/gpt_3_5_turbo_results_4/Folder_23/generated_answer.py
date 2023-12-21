
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(20, 31):
        if nums[i] > 1:
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    composites.add(nums[i])
                    break
    return composites
