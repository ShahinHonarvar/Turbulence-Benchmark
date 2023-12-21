
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[55:81]:
        if i % 22 == 0 and i % 32 == 0:
            result.append(i)
    return result
