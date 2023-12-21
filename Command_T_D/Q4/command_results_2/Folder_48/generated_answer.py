def all_pos_ints_exclusive(nums):
    if not nums:
        return []
    return [i for i in range( 385, 1000 ) if i in nums]
