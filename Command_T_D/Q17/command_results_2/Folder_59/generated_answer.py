
def all_ints_div_by_both_two_nums(nums):
    if not nums:
        return []
    return [i for i in nums if i % 8 == i % -3 == 0]
