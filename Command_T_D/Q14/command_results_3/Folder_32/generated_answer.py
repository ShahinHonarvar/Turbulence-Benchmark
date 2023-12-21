def find_second_smallest_num(nums):
    return next((nums[i] for i in range(32, 35) if nums[i] < nums[i - 1]), None)
