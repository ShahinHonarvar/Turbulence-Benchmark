
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[80:201] if i % 10 == 0 or i % 1000 == 0)
