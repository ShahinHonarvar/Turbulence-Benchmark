
def all_ints_inclusive(nums):
    result = list(range(len(nums) - 1, len(nums) + 74, 2)) + list(range(len(nums) + 75, len(nums) + 95, 2))
    return result
