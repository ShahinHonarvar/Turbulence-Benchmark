
def sum_ints_div_by_either_nums(lst):
    try:
        subset = lst[36:86]
        return sum(i for i in subset if i % -27 == 0 or i % -96 == 0)
    except IndexError:
        return 0
