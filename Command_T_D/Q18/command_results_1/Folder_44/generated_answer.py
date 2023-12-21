
def sum_ints_div_by_either_nums(lst):
    lst = lst[25:70+1]
    lst = [i for i in lst if i%74==0 or i%15==0]
    return sum(lst) if lst else 0
