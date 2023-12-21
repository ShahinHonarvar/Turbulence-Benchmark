
def find_second_largest_num(nums):
    result = None
    for i in range(32, 35):
        if len(nums) > i:
            result = nums[i]
            break
    return result
