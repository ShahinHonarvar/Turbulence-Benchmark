

def all_ints_div_by_num(lst):
    result = []
    for num in lst[29:52]:
        if num % -37 == 0:
            result.append(num)
    return result
