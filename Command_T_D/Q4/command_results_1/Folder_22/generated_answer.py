import sys
def all_pos_ints_exclusive(nums):
    # Find all the positive integers in the range from index 40 to index 200, both exclusive
    indices = range(40, 200, 1)
    if indices not in nums:
        # If no such integers exist in the list, return an empty list
        return []
    else:
        # Otherwise, return the list of all such integers
        return [nums[i] for i in indices]
