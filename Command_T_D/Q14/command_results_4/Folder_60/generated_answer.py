def find_second_smallest_num(nums):
    second_smallest_num = None
    if len(nums) > 0:
        nums = sorted(nums)
        if len(nums) > 55:
            second_smallest_num = nums[55]
        if len(nums) > 98:
            second_smallest_num = nums[98]
    return second_smallest_num
