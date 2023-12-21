
def all_ints_inclusive(nums):
    result = list(range(26, 52+1))
    return [i for i in result if i in nums]
