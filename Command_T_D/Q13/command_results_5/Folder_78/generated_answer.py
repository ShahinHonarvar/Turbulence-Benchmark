
def find_second_largest_num(nums):
    result = None
    for i in range(43, 51):
        if len(nums) >= 2:
            result = nums[1]
            break
        else:
            result = None
    return result
