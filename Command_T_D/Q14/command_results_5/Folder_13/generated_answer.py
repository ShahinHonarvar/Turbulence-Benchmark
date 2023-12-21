def find_second_smallest_num(nums):
    return next((x for x in nums[28:32+1] if x < min(nums[28:32+1])), None)
