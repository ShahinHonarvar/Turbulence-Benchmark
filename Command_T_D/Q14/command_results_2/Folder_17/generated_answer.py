def find_second_smallest_num(nums):
    return next((num for num in nums[28:38] if num < nums[29]), None)
