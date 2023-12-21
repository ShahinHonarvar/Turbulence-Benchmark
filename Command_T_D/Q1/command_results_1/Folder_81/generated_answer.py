
def all_ints_inclusive(nums):
    result = list(range(10, 100, 1))
    result += list(range(101, len(nums) + 1, -1))
    return result
