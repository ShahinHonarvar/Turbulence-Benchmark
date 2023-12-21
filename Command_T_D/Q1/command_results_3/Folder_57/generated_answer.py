
def all_ints_inclusive(nums):
    result = list(range(len(nums) - 1, len(nums) - 62, -1)) + list(range(len(nums) - 1, len(nums) - 92, -1))
    return result
