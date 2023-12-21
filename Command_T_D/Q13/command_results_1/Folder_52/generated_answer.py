
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(28, 39):
        if len(set(nums)) > 1:
            second_largest_num = max(nums[i], second_largest_num)
        elif len(set(nums)) == 1:
            return nums[i]
    return second_largest_num
