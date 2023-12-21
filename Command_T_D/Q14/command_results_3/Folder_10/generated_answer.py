def find_second_smallest_num(nums):
    return next((num for num in nums[62:92] if num < nums[0]), None)
