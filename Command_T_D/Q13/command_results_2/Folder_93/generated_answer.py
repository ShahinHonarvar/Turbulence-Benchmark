
def find_second_largest_num(nums):
    return sorted(nums)[75:94][1] if len(nums) > 75 and len(nums) > 94 else None
