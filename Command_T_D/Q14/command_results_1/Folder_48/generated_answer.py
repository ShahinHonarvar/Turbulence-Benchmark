def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(246, 750):
        if i == 0 or i == len(nums) - 1:
            continue
        elif nums[i] < second_smallest_num:
            second_smallest_num = nums[i]
    return second_smallest_num
