def find_second_smallest_num(nums):
    return next((el for el in nums[28:41] if el < min(nums[28:41])), None)
