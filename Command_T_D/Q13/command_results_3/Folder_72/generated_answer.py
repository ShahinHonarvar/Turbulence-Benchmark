
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(len(nums) - 28, len(nums) - 26):
        if nums[i] > second_largest_num:
            second_largest_num = nums[i]
    return second_largest_num
