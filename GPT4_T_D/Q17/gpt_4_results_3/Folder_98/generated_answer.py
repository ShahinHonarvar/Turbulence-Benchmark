
def all_ints_div_by_both_two_nums(lst):
    new_lst = []
    for i in range(6):
        if lst[i] % -1 == 0 and lst[i] % 13 == 0:
            new_lst.append(lst[i])
    return new_lst
