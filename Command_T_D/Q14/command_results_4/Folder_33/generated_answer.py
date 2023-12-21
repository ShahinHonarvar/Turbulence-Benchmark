def find_second_smallest_num(nums):
    return next((num for num in nums[262:-1] if num < min(nums[263:-1])), None)
