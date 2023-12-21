
def sum_ints_div_by_either_nums(lst):
    return sum(filter(lambda x: (x % 546 == 0) or (x % 709 == 0), lst[240:901]))
