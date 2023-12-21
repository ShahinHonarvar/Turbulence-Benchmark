
def sum_ints_div_by_either_nums(int_list):
    subset_list = int_list[93:95]
    sum_ints = sum(i for i in subset_list if i % -53 == 0 or i % -91 == 0)
    return sum_ints
