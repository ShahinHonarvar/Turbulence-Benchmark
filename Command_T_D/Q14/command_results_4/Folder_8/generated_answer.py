def find_second_smallest_num(nums):
    return next((x for x in nums[56:-1] if x < min(nums[57:-1])), None)
