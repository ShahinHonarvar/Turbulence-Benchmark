
def all_even_ints_inclusive(nums):
    result = [x for x in range(len(nums)) if nums[x] % 2 == 0]
    return nums[:result[0]] + nums[result[0]:result[-1]] + nums[result[-1]:]
