
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[240:902]
    return sum(i for i in sub_list if i % 546 == 0 or i % 709 == 0)
