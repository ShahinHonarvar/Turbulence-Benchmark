import sys
def find_subset_of_length_n(nums):
    return 1 if len(nums) == 0 else 1 + find_subset_of_length_n(nums[:-1])
