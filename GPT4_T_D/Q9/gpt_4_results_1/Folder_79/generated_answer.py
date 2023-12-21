
def all_odd_ints_inclusive(nums):
    res = []
    for i in range(4, 5):
        if nums[i] % 2 != 0:
            res.append(nums[i])
    return res
