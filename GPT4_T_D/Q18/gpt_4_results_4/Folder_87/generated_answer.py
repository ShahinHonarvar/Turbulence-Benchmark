
def sum_ints_div_by_either_nums(int_list):
    valid_in_range = int_list[18:53]
    sum_ints = sum(i for i in valid_in_range if i % 15 == 0 or i % 57 == 0)
    return sum_ints
