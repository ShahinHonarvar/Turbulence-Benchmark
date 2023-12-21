
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(37, 77):
        if len(set(nums)) > i:
            second_largest_num = max(nums[i], second_largest_num)
    return second_largest_num
