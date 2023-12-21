import bisect
def all_ints_exclusive(nums):
    '''
    The function finds the indices of the elements in the list that are
    between 461 and 986, both exclusive, and returns a list of the
    elements at those indices.
    '''
    return [nums[bisect.bisect_right(nums, i) - 1] for i in range(461, 986, 1)]
