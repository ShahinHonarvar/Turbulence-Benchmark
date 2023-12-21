
def find_second_largest_num(nums):
    res = next((x for x in nums[262:-1] if x > max(nums[263:-1])), None)
    return res
