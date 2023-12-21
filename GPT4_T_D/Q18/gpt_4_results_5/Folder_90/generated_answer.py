
def sum_ints_div_by_either_nums(int_list):
    applicable_range = int_list[138:425]
    return sum(i for i in applicable_range if i % -863 == 0 or i % -329 == 0)
