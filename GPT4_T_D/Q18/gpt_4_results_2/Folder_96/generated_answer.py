
def sum_ints_div_by_either_nums(ints_list):
    return sum(i for i in ints_list[50:201] if i % -34 == 0 or i % 64 == 0)
