def find_second_smallest_num(nums):
    if len(nums) < 29:
        return None
    second_smallest_num = nums[28]
    for i in range(29, 39):
        if nums[i] < second_smallest_num:
            second_smallest_num = nums[i]
    return second_smallest_num
