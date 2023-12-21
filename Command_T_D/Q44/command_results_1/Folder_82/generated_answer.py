def composite_nums_between_indices(nums):
    result = set()
    for i in range(30, len(nums) + 1):
        if i in result:
            continue
        x = nums[i]
        while x in result:
            x += nums[i]
        result.add(x)
    return result
