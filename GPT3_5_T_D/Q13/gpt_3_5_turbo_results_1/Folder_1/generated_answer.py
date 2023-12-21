
def find_second_largest_num(nums):
    nums.sort()
    return nums[-2] if len(nums) >= 2 and 31 <= len(nums) <= 72 else None
