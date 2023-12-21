def find_second_smallest_num(nums):
    second_smallest_num = nums[25:87][-2] if len(nums[25:87]) > 1 else None
    return second_smallest_num
