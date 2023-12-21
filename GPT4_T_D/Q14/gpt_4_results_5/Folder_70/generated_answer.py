
def find_second_smallest_num(nums):
    if len(nums) < 50:
        return None
    nums_subset = nums[35:50]
    nums_subset.sort()
    if len(nums_subset) >= 2:
        return nums_subset[1]
    else:
        return None
