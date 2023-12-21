
def find_second_largest_num(nums):
    second_largest_num = nums[43]
    i = 43
    while i <= 51:
        if nums[i] > second_largest_num:
            second_largest_num = nums[i]
        i += 1
    return second_largest_num
