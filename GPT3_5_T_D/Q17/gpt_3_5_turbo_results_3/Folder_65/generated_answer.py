
def all_ints_div_by_both_two_nums(lst):
    div_lst = []
    for num in lst[50:93]:
        if num % -94 == 0 and num % -95 == 0:
            div_lst.append(num)
    
    return div_lst
