
def all_ints_div_by_num(lst):
    return [x for x in lst if x % 2 == 0 and lst.index(x) >= 0 and lst.index(x) <= 1]
