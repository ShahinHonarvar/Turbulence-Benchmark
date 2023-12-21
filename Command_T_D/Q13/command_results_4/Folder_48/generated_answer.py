
def find_second_largest_num(nums):
    return nums[nums.index(sorted(nums)[533:605]) - 1] if len(nums) > 600 else None
