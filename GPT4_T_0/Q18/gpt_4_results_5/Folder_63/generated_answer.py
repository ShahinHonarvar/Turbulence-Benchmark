
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[31:51] if i % 81 == 0 or i % 64 == 0)
