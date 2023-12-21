
def all_ints_inclusive(nums):
    result = list(range(len(nums) + 1))
    return nums[:result[-1]] + nums[result[-1]:]
