def all_pos_ints_inclusive(nums):
    res = [nums[i] for i in range(1, len(nums)+1)]
    return res if all(x > 0 for x in res) else []
