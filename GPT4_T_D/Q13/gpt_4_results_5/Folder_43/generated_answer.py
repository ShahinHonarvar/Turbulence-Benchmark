
def find_second_largest_num(nums):
    nums_slice = nums[68:87]
    if len(nums_slice) < 2:
        return None
    else:
        return sorted(nums_slice)[-2]
