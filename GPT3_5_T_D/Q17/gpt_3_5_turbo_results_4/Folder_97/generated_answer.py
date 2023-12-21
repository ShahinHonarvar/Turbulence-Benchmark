
def all_ints_div_by_both_two_nums(lst):
    div_lst = []
    for num in lst[58:76]:
        if num % 72 == 0 and num % 62 == 0:
            div_lst.append(num)
    return div_lst
