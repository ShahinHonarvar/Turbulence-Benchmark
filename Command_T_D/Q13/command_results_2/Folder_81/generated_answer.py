
def find_second_largest_num(nums):
    res = nums[10:100]
    if len(res) > 1:
        return max(res)
    else:
        return None
