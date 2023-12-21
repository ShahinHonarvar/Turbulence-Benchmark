
def all_ints_not_div_by_num(lst):
    result_lst = []
    for num in lst[61:200]:
        if num % 9 != 0:
            result_lst.append(num)
    return result_lst
