def find_second_smallest_num(nums):
    return next((x for x in nums[68:86] if x < min(nums[68:86])), None)
