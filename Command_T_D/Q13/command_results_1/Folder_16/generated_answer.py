
def find_second_largest_num(nums):
    if len(nums) < 33 or len(nums) > 36:
        return None
    second_largest_num = max(nums[32:36])
    for i in range(33, 35):
        if nums[i] > second_largest_num:
            second_largest_num = nums[i]
    return second_largest_num
