
def sum_ints_div_by_either_nums(ints_list):
    return sum(i for i in ints_list[90:201] if i % 13 == 0 or i % -31 == 0)
