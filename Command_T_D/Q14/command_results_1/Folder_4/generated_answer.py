def find_second_smallest_num(nums):
    return next((num for num in nums[70:84] if num < min(nums[70:84])), None)
