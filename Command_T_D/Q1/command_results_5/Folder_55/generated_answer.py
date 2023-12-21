
def all_ints_inclusive(nums):
    result = [x for x in range(len(nums)) if x >= 0 and x < 11]
    return nums[:result[-1] + 1] + nums[result[-1]:]
