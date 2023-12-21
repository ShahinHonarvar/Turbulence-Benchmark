
def sum_odd_ints_inclusive(nums):
    if len(nums) < 36:
        return 0
    else:
        return sum([i for i in nums[32:36] if i % 2 != 0])
