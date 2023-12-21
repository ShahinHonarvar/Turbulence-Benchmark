def find_second_smallest_num(nums):
    return next((nums[i] for i in range(52, 71) if i > 0 and nums[i - 1] > nums[i]), None)
