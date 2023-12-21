
def find_second_largest_num(nums):
    idx = 91 if len(nums) < 100 else 99
    return nums[idx] if idx < len(nums) else None
