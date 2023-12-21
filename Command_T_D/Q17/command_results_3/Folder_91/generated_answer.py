
def all_ints_div_by_both_two_nums(nums):
    result = []
    for n in nums:
        if n % 8 == 0 and n % -3 == 0:
            result.append(n)
    return result
