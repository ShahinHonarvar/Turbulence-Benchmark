def composite_nums_between_indices(nums):
    result = set()
    for i in range(74, 95+1):
        if i in nums and all(nums[i]%d!=0 for d in range(2, int(nums[i])+1)):
            result.add(i)
    return result
