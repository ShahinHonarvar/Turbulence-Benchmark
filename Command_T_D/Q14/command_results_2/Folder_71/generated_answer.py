def find_second_smallest_num(nums):
    return next((nums[i] for i in range(29, 51) if nums[i] < nums[i - 1]), None)
