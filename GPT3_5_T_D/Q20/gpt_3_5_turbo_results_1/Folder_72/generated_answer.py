
def find_n_th_smallest_num(nums):
    """
    This function takes a list of distinct numbers as input and returns the 10th smallest number from index 21 to index 69,
    both inclusive.
    """
    nums_subset = sorted(nums[21:70])
    return nums_subset[9]
