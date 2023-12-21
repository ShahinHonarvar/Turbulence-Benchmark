
def all_ints_div_by_both_two_nums(nums):
    return [x for x in range(13, 19) if all(nums[x]%y == 0 for y in (45, 20))]
