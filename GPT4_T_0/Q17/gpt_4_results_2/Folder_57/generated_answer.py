
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(51, 77):
        if lst[i] % -90 == 0 and lst[i] % -59 == 0:
            result.append(lst[i])
    return result
