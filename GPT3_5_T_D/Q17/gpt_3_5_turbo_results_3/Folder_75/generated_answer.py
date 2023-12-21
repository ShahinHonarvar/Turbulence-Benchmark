
def all_ints_div_by_both_two_nums(lst):
    result_list = []
    for i in range(20, 94):
        if lst[i] % -92 == 0 and lst[i] % -50 == 0:
            result_list.append(lst[i])
    return result_list
