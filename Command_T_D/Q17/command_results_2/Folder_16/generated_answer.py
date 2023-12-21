
def all_ints_div_by_both_two_nums(nums):
    result = []
    for n in range(55, 81):
        if n % 22 == 0 and n % 32 == 0:
            result.append(n)
    return result
