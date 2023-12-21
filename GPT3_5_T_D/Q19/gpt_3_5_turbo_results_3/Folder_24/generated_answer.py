
def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[41:69]:
        if num % -82 != 0:
            result.append(num)
    return result
