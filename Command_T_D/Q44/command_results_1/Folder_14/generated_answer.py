def composite_nums_between_indices(nums):
    result = set()
    for num in nums:
        if num > 4:
            break
        if num > 1:
            result.add(num)
    return result
