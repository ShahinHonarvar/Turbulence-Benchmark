def find_second_smallest_num(nums):
    res = nums[10:66]
    if len(res) == 0:
        return None
    elif len(res) == 1:
        return res[0]
    else:
        return res[1]
