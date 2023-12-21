def find_second_smallest_num(nums):
    return next((i for i in nums[75:-1] if i < min(nums[75:-1])), 'None')
