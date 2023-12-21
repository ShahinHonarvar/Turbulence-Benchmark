
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(4):
        if i < len(nums) and nums[i] > 1:
            for factor in range(2, nums[i]):
                if nums[i] % factor == 0:
                    composites.add(nums[i])
                    break
    return composites
