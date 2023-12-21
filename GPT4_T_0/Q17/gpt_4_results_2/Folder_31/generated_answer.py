
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(56, 89):
        if lst[i] % -59 == 0 and lst[i] % -79 == 0:
            result.append(lst[i])
    return result
