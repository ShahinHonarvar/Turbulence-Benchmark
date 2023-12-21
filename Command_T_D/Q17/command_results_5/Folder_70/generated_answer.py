
def all_ints_div_by_both_two_nums(nums):
    result = []
    for n in range(42, 43):
        if n % 15 == 0 and n % 87 == 0:
            result.append(n)
    return result
