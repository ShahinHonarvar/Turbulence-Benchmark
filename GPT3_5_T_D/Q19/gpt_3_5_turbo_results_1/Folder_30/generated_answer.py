
def all_ints_not_div_by_num(lst):
    lst = lst[20:35]
    new_lst = []
    for num in lst:
        if num % -36 != 0:
            new_lst.append(num)
    return new_lst
