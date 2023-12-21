
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(len(nums) - 1, -1, -1):
        if i == 32 or i == 33 or i == 34 or i == 35:
            if nums[i] > second_largest_num:
                second_largest_num = nums[i]
    return second_largest_num
