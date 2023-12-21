def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(40, 81):
        if i == 40:
            second_smallest_num = nums[i]
        elif i == 81:
            second_smallest_num = nums[i]
        elif nums[i] < second_smallest_num:
            second_smallest_num = nums[i]
        elif nums[i] == second_smallest_num:
            second_smallest_num = nums[i]
    return second_smallest_num
