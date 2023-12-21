
def all_ints_div_by_both_two_nums(nums):
    if not nums:
        return []
    for i in range(32, 100):
        if nums[i] % -11 == 0 and nums[i] % -15 == 0:
            yield nums[i]
    return
