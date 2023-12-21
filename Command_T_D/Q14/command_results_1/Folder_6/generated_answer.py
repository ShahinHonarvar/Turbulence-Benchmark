def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(29, 79):
        if len(set(nums)) >= 2 and nums[i] < nums[0]:
            second_smallest_num = nums[i]
            break
    return second_smallest_num
