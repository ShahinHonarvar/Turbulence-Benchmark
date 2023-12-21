
def find_second_largest_num(nums):
    second_largest_num = max(nums[43:86]) if 43 < len(nums) - 86 else None
    return second_largest_num
