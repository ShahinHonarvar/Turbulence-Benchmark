import itertools
def all_pos_ints_inclusive(nums):
    if 25 <= len(nums) <= 87:
        return [i for i in range(25, 87+1)]
    else:
        return []
