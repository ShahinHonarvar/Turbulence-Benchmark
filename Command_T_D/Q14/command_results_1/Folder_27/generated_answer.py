def find_second_smallest_num(nums):
    return next((y for x, y in zip(nums[25:59], nums[26:]) if y < x), None)
