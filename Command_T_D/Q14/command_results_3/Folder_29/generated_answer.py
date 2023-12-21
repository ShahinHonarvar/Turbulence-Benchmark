def find_second_smallest_num(nums):
    return next(i for i in range(55, 98) if nums[i] < nums[-1])
