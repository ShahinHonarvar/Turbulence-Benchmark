
def find_second_largest_num(nums):
    return nums[max(0, 310 - 1) : min(370 + 1, len(nums))] + [None]
