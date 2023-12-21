
def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[19:49]:
        if num % -36 != 0:
            result.append(num)
    return result
