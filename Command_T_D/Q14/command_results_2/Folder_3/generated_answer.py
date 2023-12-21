def find_second_smallest_num(nums):
    return next((x for x in nums[27:55] if x < min(nums[27:55])), None)
