def find_second_smallest_num(nums):
    return next(num for num in nums[74:95] if num < nums[73])
