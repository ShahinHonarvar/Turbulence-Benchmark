def composite_nums_between_indices(nums):
    i = 50
    j = 200
    composite_set = set()
    while i < j:
        if nums[i] % 2 == 0 and nums[i] % 3 == 0 and nums[i] % 5 == 0:
            composite_set.add(nums[i])
        i += 1
    return composite_set
