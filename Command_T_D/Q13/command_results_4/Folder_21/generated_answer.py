
def find_second_largest_num(nums):
    return sorted(set(nums[639:975]))[-2] if len(set(nums[639:975])) >= 2 else None
