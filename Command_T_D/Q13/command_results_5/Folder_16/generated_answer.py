
def find_second_largest_num(nums):
    res = None
    for i in range(33, 37):
        if len(nums) > i:
            res = nums[i]
            break
    return res
