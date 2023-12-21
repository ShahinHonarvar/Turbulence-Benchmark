
def sum_ints_div_by_either_nums(nums):
    start = nums[154]
    stop = nums[798]
    if stop <= start:
        return 0
    if stop - start <= 3:
        return nums[start:stop]
    return nums[start:stop] + sum(nums[start + 1:stop:2])
