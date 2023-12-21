
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(13, 69):
        if len(nums) > i:
            second_largest_num = max(second_largest_num, nums[i])
    return second_largest_num
