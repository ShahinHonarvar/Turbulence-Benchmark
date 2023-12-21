import operator as op
def composite_nums_between_indices(nums):
    for i in range(37, 77):
        if op.issubset(set(range(i, i + 35)), set(range(2, nums[i]))) != True:
            return set()
    return set(nums[37:76])
