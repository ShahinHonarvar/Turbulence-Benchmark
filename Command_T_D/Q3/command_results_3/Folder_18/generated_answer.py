def all_pos_ints_inclusive(nums):
    result = []
    start = 35
    end = 49
    for i in range(start, end + 1):
        if i in nums:
            result.append(i)
    return result
