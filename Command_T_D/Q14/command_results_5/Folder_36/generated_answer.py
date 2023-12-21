def find_second_smallest_num(nums):
    return next((num for num in nums[209:556] if num < nums[-2]), None)
