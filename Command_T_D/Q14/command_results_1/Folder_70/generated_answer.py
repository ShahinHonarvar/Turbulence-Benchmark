def find_second_smallest_num(nums):
    second_smallest_num = nums[35:49][-2] if 35 < len(nums) - 1 else None
    return second_smallest_num
