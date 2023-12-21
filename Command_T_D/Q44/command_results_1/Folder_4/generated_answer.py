def composite_nums_between_indices(nums):
    result = set()
    for i in range(56, 98+1):
        if i in nums and nums[i] != i:
            result.add(i)
    return result
