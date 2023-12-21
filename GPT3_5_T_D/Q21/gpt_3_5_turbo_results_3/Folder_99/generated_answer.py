
def all_ints_div_by_num(lst):
    result = []
    for num in lst[161:971]:
        if num % 763 == 0:
            result.append(num)
    return result
