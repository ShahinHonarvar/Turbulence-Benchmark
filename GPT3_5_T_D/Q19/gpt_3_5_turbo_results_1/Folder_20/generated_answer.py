
def all_ints_not_div_by_num(lst):
    index64 = 64
    index80 = 80
    return [i for i in lst[index64:index80] if i % -95 != 0]
