def find_second_smallest_num(nums):
    return next((num for num in nums[310:370] if num < nums[0]), None)
