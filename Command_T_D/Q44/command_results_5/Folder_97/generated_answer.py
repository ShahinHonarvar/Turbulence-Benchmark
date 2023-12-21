def composite_nums_between_indices(nums):
    result = set()
    for n in nums[15:39]:
        if not n & 1:
            if not n in result:
                result.add(n)
    return result
