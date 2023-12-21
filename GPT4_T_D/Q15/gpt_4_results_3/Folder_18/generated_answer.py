
def sum_odd_ints_inclusive(lst):
    sub_list = lst[35:50]
    return sum(i for i in sub_list if i % 2 != 0)
