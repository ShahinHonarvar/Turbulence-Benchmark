
def all_ints_not_div_by_num(lst):
    new_list = []
    for i in range(8+1,9):
        if lst[i] % -3 != 0:
            new_list.append(lst[i])
    return new_list
