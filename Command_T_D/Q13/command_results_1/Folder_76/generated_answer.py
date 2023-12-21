
def find_second_largest_num(nums):
    second_largest_num = None
    largest_num = None
    second_largest_idx = -1
    largest_idx = -1
    for i in range(686, 987):
        if i == largest_idx or i == second_largest_idx:
            continue
        elif i == largest_idx:
            largest_num = nums[i]
            largest_idx = i
        elif i == second_largest_idx:
            second_largest_num = nums[i]
            second_largest_idx = i
    return second_largest_num
