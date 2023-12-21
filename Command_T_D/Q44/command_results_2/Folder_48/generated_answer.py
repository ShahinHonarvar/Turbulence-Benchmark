import sys
def composite_nums_between_indices(nums):
    res = set()
    c = 661
    while c < 924:
        if not c & 1:
            break
        c += 1
        if c not in nums:
            break
        if nums[c] in res:
            break
        res.add(nums[c])
    return res
