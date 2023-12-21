def find_second_smallest_num(nums):
    return next((num for i, num in enumerate(nums) if num == sorted(nums)[-2]), None)
