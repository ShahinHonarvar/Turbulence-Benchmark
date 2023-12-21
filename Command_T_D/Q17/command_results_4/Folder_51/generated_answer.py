
def all_ints_div_by_both_two_nums(list):
    list = list[6:9]
    return [n for n in list if n % -1 == 0 and n % -10 == 0]
