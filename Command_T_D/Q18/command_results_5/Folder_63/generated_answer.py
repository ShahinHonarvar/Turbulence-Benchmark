
def sum_ints_div_by_either_nums(lst):
    lst_31_50 = lst[30:51]
    lst_81 = [i for i in lst_31_50 if i % 81 == 0]
    lst_64 = [i for i in lst_31_50 if i % 64 == 0]
    return sum(lst_81 + lst_64) if lst_81 or lst_64 else 0
