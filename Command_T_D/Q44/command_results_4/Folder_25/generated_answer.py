def composite_nums_between_indices(nums):
    result = set()
    for num in nums[75:94]:
        if num > 1 and num > 2 and num > 3:
            result.add(num)
    return result
