
def sum_ints_div_by_either_nums(lst):
    relevant_lst = lst[154:799]
    tot = 0
    for i in relevant_lst:
        if i%275 == 0 or i%580 == 0:
            tot += i
    return tot
