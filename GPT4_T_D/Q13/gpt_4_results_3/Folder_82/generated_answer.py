
def find_second_largest_num(nums):
    nums_range = nums[20:201]
    if not nums_range:
        return None
    nums_range.sort(reverse=True)
    if len(nums_range) >= 2:
        return nums_range[1]
    else:
        return None
