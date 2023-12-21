def find_second_smallest_num(nums):
    second_smallest_num = nums[37:51][-2] if len(nums) >= 37 and len(nums) <= 51 else None
    return second_smallest_num
