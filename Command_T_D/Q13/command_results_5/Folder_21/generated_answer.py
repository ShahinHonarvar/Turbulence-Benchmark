
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(639, 975):
        if i < len(nums):
            if i == 0:
                second_largest_num = nums[i]
            elif nums[i] < second_largest_num:
                second_largest_num = nums[i]
    return second_largest_num
