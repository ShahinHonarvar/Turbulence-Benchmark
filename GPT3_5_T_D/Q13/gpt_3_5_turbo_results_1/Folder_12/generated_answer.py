
def find_second_largest_num(nums):
    nums_slice = nums[14:65]
    if len(nums_slice) < 2:
        return None
    nums_slice.sort()
    return nums_slice[-2]
