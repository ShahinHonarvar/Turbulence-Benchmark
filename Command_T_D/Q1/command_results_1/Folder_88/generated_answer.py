
def all_ints_inclusive(nums):
    return list(range(3, nums.count(nums[2]) + 3, 2))
