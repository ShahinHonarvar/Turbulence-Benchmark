
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:16]), start=16) - 16]
