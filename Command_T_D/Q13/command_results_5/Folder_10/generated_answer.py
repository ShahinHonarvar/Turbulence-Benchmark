
def find_second_largest_num(nums):
    result = nums[25:59]
    if len(result) > 1:
        result.sort()
        return result[1]
    elif len(result) == 1:
        return result[0]
    else:
        return None
