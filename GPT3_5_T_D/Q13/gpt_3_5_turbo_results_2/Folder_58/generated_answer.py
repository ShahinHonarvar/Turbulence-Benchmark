
def find_second_largest_num(nums):
    nums_slice = nums[209:557]
    nums_slice.sort()
    if len(nums_slice) < 2:
        return None
    return nums_slice[-2]
