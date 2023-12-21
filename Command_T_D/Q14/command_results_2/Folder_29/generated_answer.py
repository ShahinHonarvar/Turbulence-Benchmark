def find_second_smallest_num(nums):
    return next((nums[55:98] + nums[:55])[1], None)
