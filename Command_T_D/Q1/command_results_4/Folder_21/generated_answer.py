
def all_ints_inclusive(nums):
    result = nums[527:538] + nums[527:0:-1] + nums[538:527:-1]
    return result
