
def sum_ints_div_by_either_nums(int_list):
    subset_list = int_list[70:201]
    sum_divisibles = sum(i for i in subset_list if i % 3 == 0 or i % -300 == 0)
    return sum_divisibles
