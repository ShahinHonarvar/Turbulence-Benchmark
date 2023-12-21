
def all_ints_div_by_num(lst):
    div_by_26 = [i for i in lst[25:60] if i % -26 == 0]
    return div_by_26
