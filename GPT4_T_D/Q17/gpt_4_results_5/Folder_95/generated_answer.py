
def all_ints_div_by_both_two_nums(lst):
    div_lst = []
    for i in lst[57:85]:
        if i % -30 == 0 and i % -88 == 0:
            div_lst.append(i)
    return div_lst
