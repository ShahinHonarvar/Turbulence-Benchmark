
def sum_ints_div_by_either_nums(lst):
    lst_new = [n for n in lst if n % 55 == 0 or n % 10 == 0]
    return sum(lst_new[58:81])
