
def find_second_largest_num(nums):
    result = None
    if len(nums) > 22 and len(nums) > 50:
        result = nums[22]
        if len(nums) > 23:
            result = nums[23]
    return result
