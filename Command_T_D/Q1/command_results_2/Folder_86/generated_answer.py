
def all_ints_inclusive(nums):
    result = [i for i in range(40, 80 + 1)]
    return [nums[i - 1] for i in result]
