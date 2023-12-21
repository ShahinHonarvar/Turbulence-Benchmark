
def sum_ints_div_by_either_nums(lst):
    subset_lst = lst[2:8]
    sum_nums = sum([i for i in subset_lst if i % -1 == 0 or i % -7 == 0])
    
    return sum_nums if sum_nums != 0 else 0
