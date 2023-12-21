def find_second_smallest_num(nums):
    return next((el for el in nums[66:93] if el < min(nums[66:93])), None)
