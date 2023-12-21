import itertools
def all_pos_ints_inclusive(nums):
    for i in range(min(nums), max(nums) + 1):
        if i in nums:
            yield i
    for i in range(min(nums), max(nums) + 1):
        for j in range(i, max(nums) + 1):
            if j in nums:
                yield i
                yield j
