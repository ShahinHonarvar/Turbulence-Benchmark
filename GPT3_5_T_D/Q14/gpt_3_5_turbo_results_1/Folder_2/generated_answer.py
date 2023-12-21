
def find_second_smallest_num(nums):
    nums_range = nums[43:87]
    if len(nums_range) < 2:
        return None
    else:
        nums_range.sort()
        return nums_range[1]
