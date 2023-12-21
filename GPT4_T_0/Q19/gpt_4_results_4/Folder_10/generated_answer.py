
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(87, 89):
        if lst[i] % -61 != 0:
            result.append(lst[i])
    return result
