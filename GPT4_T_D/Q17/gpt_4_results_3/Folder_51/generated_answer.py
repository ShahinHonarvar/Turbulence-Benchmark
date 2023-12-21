
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[6:10]:
        if i % -1 == 0 and i % -10 == 0:
            result.append(i)
    return result
