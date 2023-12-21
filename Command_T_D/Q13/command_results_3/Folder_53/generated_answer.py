
def find_second_largest_num(nums):
    return sorted(nums)[-2] if len(nums) > 100 and len(nums) > 200 else None
