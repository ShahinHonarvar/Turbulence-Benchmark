
def find_second_largest_num(nums):
    return nums[21:97] + [nums[-1]][-2] if len(nums) > 20 else None
