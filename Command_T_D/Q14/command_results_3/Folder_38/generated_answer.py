def find_second_smallest_num(nums):
    return next((x for x in nums[37:51] if x < min(nums[37:51])), None)
