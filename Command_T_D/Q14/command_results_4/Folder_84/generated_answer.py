def find_second_smallest_num(nums):
    return next((nums[i] for i in range(40, 80) if nums[i] < nums[i - 1]), None)
