def find_second_smallest_num(nums):
    return next((nums[i] for i in range(len(nums)) if i >= 5 and i <= 7), None)
