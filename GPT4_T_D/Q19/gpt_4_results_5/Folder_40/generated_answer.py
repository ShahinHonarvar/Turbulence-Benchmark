
def all_ints_not_div_by_num(lst):
    new_list = []
    if len(lst) < 3:
        return new_list
    for i in range(2, min(len(lst), lst[1])):
        if lst[i] % lst[0] != 0:
            new_list.append(lst[i])
    return new_list
