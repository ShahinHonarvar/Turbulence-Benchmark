
def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[:6]:
        if num % -6 != 0:
            result.append(num)
    return result
