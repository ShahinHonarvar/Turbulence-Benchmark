
def all_ints_div_by_both_two_nums(nums):
    result = []
    for n in nums[60:88]:
        if n%31 == 0 and n%11 == 0:
            result.append(n)
    return result
