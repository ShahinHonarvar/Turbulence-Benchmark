
def find_second_largest_num(nums):
    nums_subset = nums[209:557]
    nums_subset.sort()
    return nums_subset[-2] if len(nums_subset) >= 2 else None
