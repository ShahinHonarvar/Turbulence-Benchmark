
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(12, 92+1):
        if i < len(nums) and nums[i] > second_largest_num:
            second_largest_num = nums[i]
    return second_largest_num
