
def sum_ints_div_by_either_nums(int_list):
    part_of_list = int_list[69:71]
    sum_divisible = sum(i for i in part_of_list if i%72==0 or i%70==0)
    return sum_divisible
