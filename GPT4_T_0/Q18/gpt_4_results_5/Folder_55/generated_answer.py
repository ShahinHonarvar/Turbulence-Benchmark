
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[0:10] if i % 10 == 0 or i % 100 == 0)
