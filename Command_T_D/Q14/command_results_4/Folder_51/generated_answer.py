def find_second_smallest_num(nums):
    return next((x for x in nums if x < min(nums)), None)
