
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(10, 29):
        if lst[i] % -61 == 0 and lst[i] % -64 == 0:
            result.append(lst[i])
    return result
