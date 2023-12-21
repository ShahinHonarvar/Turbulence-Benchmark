
def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[38:82]:
        if num % -61 == 0 and num % -71 == 0:
            result.append(num)
    return result
