
def all_ints_not_div_by_num(lst):
    sublist = lst[496:826]
    return [x for x in sublist if x % -201 != 0]
