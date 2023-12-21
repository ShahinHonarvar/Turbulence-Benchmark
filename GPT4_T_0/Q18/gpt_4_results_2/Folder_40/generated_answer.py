
def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 2:
        return 0
    else:
        return sum(i for i in int_list[0:2] if i % 2 == 0 or i % 1 == 0)
