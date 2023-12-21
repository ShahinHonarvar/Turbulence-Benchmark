
def find_second_largest_num(nums):
    if len(nums) < 93:
        return None
    second_largest = sorted(nums[62:93])[-2] if len(nums[62:93]) > 1 else None
    return second_largest
