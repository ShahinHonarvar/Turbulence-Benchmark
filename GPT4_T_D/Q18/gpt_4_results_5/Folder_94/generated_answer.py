
def sum_ints_div_by_either_nums(int_list):
    valid_ints = [i for i in int_list[93:95] if i % -53 == 0 or i % -91 == 0]
    return sum(valid_ints) if valid_ints else 0
