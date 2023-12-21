
def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[24:33]:
        if num % 35 == 0 and num % 87 == 0:
            result.append(num)
    return result
