
def find_second_largest_num(nums):
    for i in range(42, 68):
        if len(nums) > i:
            nums[i], second_largest_num = second_largest_num, nums[i]
    return second_largest_num
