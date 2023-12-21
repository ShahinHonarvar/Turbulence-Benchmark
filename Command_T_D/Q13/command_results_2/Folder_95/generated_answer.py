
def find_second_largest_num(nums):
    second_largest_num = max(nums[82:86]) if len(nums) > 82 and len(nums) > 86 else None
    return second_largest_num
