
def all_ints_div_by_both_two_nums(nums):
    result = []
    for n in nums[86:90]:
        if n % -71 == 0 and n % -67 == 0:
            result.append(n)
    return result
