def find_second_smallest_num(nums):
    return next(nums[533:605].sort()[:2])
