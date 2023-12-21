
def sum_ints_div_by_either_nums(lst):
    subset = lst[57:85]
    result = 0
    for num in subset:
        if num % -30 == 0 or num % -88 == 0:
            result += num
    return result
