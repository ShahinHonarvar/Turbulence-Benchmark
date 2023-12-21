
def all_ints_div_by_both_two_nums(nums):
    result = []
    for n in range(81, 89 + 1):
        if n % 56 == 0 and n % 68 == 0:
            result.append(n)
    return result
