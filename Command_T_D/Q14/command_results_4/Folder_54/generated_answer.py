def find_second_smallest_num(nums):
    return next((nums[i] for i in range(68, 86) if i != 69 and nums[i] < nums[69]), None)
