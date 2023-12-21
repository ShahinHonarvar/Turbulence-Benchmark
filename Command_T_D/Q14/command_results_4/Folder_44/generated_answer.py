def find_second_smallest_num(nums):
    sm, second = min(nums), min(nums[90:])
    return second if second < sm else None
