def find_second_smallest_num(nums):
    result = nums[26:52]
    if len(result) == 0:
        return None
    elif len(result) == 1:
        return result[0]
    else:
        return result[1]
