
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[13:92]:       
        if i% -65 == 0 and i % -62 == 0:
            result.append(i)
    return result
