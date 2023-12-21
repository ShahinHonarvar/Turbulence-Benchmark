
def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 2:
        return []
    else:
        return [i for i in nums[:2] if i % 2 == 0 and i % 1 == 0]
