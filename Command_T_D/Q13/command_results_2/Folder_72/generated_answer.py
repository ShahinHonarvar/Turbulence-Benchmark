
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(29, 51):
        if i < len(nums) - 1 and i >= 29:
            if nums[i] > second_largest_num:
                second_largest_num = nums[i]
    return second_largest_num
