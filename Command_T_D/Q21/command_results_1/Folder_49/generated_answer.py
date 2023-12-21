def all_ints_div_by_num(nums):
    if not nums:
        return []
    start = nums[30]
    stop = nums[300]
    result = []
    for i in range(start, stop + 1):
        if i % 5 == 0:
            result.append(i)
    return result
